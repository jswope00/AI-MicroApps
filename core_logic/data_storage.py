import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_gsheets import GSheetsConnection

load_dotenv()

def get_runs_data(gsheets_url, gsheets_worksheet="Sheet1"):
    
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(spreadsheet=gsheets_url, worksheet=gsheets_worksheet,ttl="0")

    return df

def post_runs_data(df,gsheets_url,gsheets_worksheet="Sheet1"):

    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.update(spreadsheet=gsheets_url, worksheet=gsheets_worksheet, data=df)
    
    st.cache_data.clear()

    return df