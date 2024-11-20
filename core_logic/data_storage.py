import streamlit as st
from dotenv import load_dotenv
from streamlit_gsheets import GSheetsConnection
from datetime import datetime
import pandas as pd
from sqlalchemy import text
from abc import ABC, abstractmethod
from typing import List
import os

load_dotenv()

class StorageHandler(ABC):
    @abstractmethod
    def get_runs_data(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def post_runs_data(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

class SQLStorageHandler(StorageHandler):
    def get_runs_data(self) -> pd.DataFrame:
        conn = st.connection("local", type='sql')
        # Query and display the data you inserted
        ma_runs = conn.query('select * from ma_runs')
        st.dataframe(ma_runs)
        return ma_runs
    
    def post_runs_data(self, df: pd.DataFrame) -> pd.DataFrame:
        conn = st.connection('local', type='sql')
        with conn.session as session:
            session.execute(text('CREATE TABLE IF NOT EXISTS `ma_runs` (date TIMESTAMP, app_title TEXT, phase_instructions TEXT, user_prompt TEXT, response TEXT, run_cost FLOAT, model TEXT);'))
            session.execute(
                text('INSERT INTO ma_runs (date, app_title, phase_instructions, user_prompt, response, run_cost, model) VALUES (:date, :app_title, :phase_instructions, :user_prompt, :response, :run_cost, :model)'),
                {
                    "date": df['timestamp'].iloc[0].to_pydatetime(),
                    "app_title": df['APP_TITLE'].iloc[0],
                    "phase_instructions": df['Phase Instructions'].iloc[0],
                    "user_prompt": df['User Prompt'].iloc[0],
                    "response": df['LLM Response'].iloc[0],
                    "run_cost": df['Run Cost'].iloc[0],
                    "model": df['model'].iloc[0]
                }
            )
            session.commit()
        return df

class GSheetsStorageHandler(StorageHandler):
    def __init__(self, gsheets_url, worksheet="Sheet1"):
        self.gsheets_url = gsheets_url
        self.worksheet = worksheet
    
    def get_runs_data(self) -> pd.DataFrame:
        conn = st.connection("gsheets", type=GSheetsConnection)
        try:
            df = conn.read(spreadsheet=self.gsheets_url, worksheet=self.worksheet, ttl="0")
            return df
        except Exception:  # This will catch worksheet not found errors
            return pd.DataFrame()  # Return empty dataframe
    
    def post_runs_data(self, df: pd.DataFrame) -> pd.DataFrame:
        conn = st.connection("gsheets", type=GSheetsConnection)
        try:
            # First get existing data
            existing_data = self.get_runs_data()
            
            # Append new data to existing data
            if existing_data.empty:
                combined_data = df
            else:
                combined_data = pd.concat([existing_data, df], ignore_index=True)
            
            # Update the sheet with combined data
            result = conn.update(spreadsheet=self.gsheets_url, worksheet=self.worksheet, data=combined_data)
        except Exception as e:
            st.error(f"Google Sheets error: {str(e)}")
            return None
        
        return result

class CompositeStorageHandler(StorageHandler):
    def __init__(self, handlers: List[StorageHandler]):
        self.handlers = handlers
    
    def get_runs_data(self) -> pd.DataFrame:
        # Return data from the first handler that has data
        for handler in self.handlers:
            data = handler.get_runs_data()
            if not data.empty:
                return data
        return pd.DataFrame()
    
    def post_runs_data(self, df: pd.DataFrame) -> pd.DataFrame:
        results = []
        errors = []

        print("Handlers:", self.handlers)
        
        # Try to post to all handlers
        for handler in self.handlers:
            try:
                result = handler.post_runs_data(df)
                if result is not None:
                    results.append(result)
            except Exception as e:
                errors.append(f"Error in {handler.__class__.__name__}: {str(e)}")
        
        if errors:
            st.warning("Some storage operations failed:\n" + "\n".join(errors))
        
        # Return the first successful result, or None if all failed
        return results[0] if results else None

class NoStorageHandler(StorageHandler):
    def get_runs_data(self) -> pd.DataFrame:
        return pd.DataFrame()
    
    def post_runs_data(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

def setup_storage(config):
    """
    Creates and returns appropriate storage handler(s) based on configuration.
    
    Args:
        config (dict): Configuration dictionary containing storage settings
        
    Returns:
        StorageHandler: Configured storage handler
    """
    storage_types = []
    
    # Check for SQL storage - env vars first, then config, default to False
    use_sql = config.get("USE_SQL", os.getenv("USE_SQL", False))
    if use_sql:
        storage_types.append("sql")
    
    # Check for GSheets storage
    use_gsheets = config.get("USE_GSHEETS", os.getenv("USE_GSHEETS", False))
    if use_gsheets:
        storage_types.append("gsheets")
    
    # If no storage type is specified, default to no storage
    if not storage_types:
        storage_types = []
    
    handler = create_storage_handler(
        storage_types,
        gsheets_url=config.get("GSHEETS_URL_OVERRIDE", os.getenv("GSHEETS_URL", None)),
        worksheet=config.get("GSHEETS_WORKSHEET_OVERRIDE", os.getenv("GSHEETS_WORKSHEET", "Sheet1"))
    )
    
    return handler


# Updated factory function to support multiple storage types
def create_storage_handler(storage_types: List[str], **kwargs) -> StorageHandler:
    if not storage_types:
        return NoStorageHandler()
    
    if len(storage_types) == 1:
        storage_type = storage_types[0].lower()
        if storage_type == "sql":
            return SQLStorageHandler()
        elif storage_type == "gsheets":
            return GSheetsStorageHandler(
                gsheets_url=kwargs.get("gsheets_url"),
                worksheet=kwargs.get("worksheet", "Sheet1")
            )
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")
    
    # Create multiple handlers for composite storage
    handlers = []
    for storage_type in storage_types:
        handlers.append(create_storage_handler([storage_type], **kwargs))
    
    return CompositeStorageHandler(handlers)

class StorageManager:
    _instance = None
    _storage = None

    @classmethod
    def initialize(cls, config):
        if cls._instance is None:
            cls._instance = cls()
            cls._storage = setup_storage(config)
        return cls._instance

    @classmethod
    def get_storage(cls):
        if cls._storage is None:
            raise RuntimeError("StorageManager not initialized. Call initialize() first")
        return cls._storage

__all__ = ['create_storage_handler', 'setup_storage', 'StorageHandler']