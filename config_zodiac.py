APP_TITLE = "Zodiac Symbol"

APP_INTRO = """This is a demonstration app that determines a user's zodiac symbol based on their birth month and date."""

APP_HOW_IT_WORKS = """
This app collects the name, birth month, and birth date of the user, and provides them their Zodiac symbol. 
It utilizes the OpenAI and other AI APIs to send a custom prompt to AI with the user's inputs and returns the AI's response.
"""

SHARED_ASSET = {}

HTML_BUTTON = {}

SYSTEM_PROMPT = """You are an expert in zodiac symbols. You know the accurate zodiac symbol based on a person's birth month and date."""

PHASES = {
    "phase1": {
        "name": "User Details",
        "fields": {
            "system": {
                "type": "radio",
                "label": "Astrology System",
                "options": ["Western", "Chinese"],
                "value": ""
            },
            "name": {
                "type": "text_input",
                "label": "What is your first name?",
                "helper": "First name only, please",
                "value": "John",
                "showIf": {"system": ["Western", "Chinese"]}
            },
            "month": {
                "type": "radio",
                "label": "What is your birth month?",
                "options": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                "showIf": {"system": "Western"}
            },
            "day": {
                "type": "number_input",
                "label": "What is your birth day?",
                "min_value": 1,
                "max_value": 31,
                "showIf": {"system": "Western"}
            },
            "year": {
                "type": "number_input",
                "label": "What is your birth year?",
                "min_value": 1900,
                "max_value": 2020,
                "showIf": {"system": ["Western", "Chinese"]}
            }
        },
        "phase_instructions": "",
        "user_prompt": [
                    {
                        "condition": {"system": "Western"},
                        "prompt": """My name is {name}. I was born on {month} {day}, {year}. Please provide me my Western zodiac symbol, and give a short horoscope for the day."""
                    },
                    {
                        "condition": {"system": "Chinese"},
                        "prompt": """My name is {name}. I was born in the year {year}. Please provide me my Chinese zodiac symbol, and give a short horoscope for the day."""
                    }
                ],
        "show_prompt": True,
        "allow_skip": True
    }
}

selected_llm = "gpt-4o-mini"

LLM_CONFIGURATIONS = {
    "gpt-4o-mini": {
        "model": "gpt-4o-mini",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.150,
        "price_output_token_1M":.600
    },
    "gpt-4-turbo": {
        "model": "gpt-4-turbo",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":10,
        "price_output_token_1M":30
    },
    "gpt-4o": {
        "model": "gpt-4o",
        "frequency_penalty": 0,
        "max_tokens": 250,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M": 5,
        "price_output_token_1M": 15
    },
    "gemini-1.0-pro": {
        "model": "gemini-1.0-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.5,
        "price_output_token_1M":1.5
    },
    "gemini-1.5-flash": {
        "model": "gemini-1.5-flash",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.35,
        "price_output_token_1M":1.05
    },
    "gemini-1.5-pro": {
        "model": "gemini-1.5-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":3.5,
        "price_output_token_1M":10.50
    },
    "claude-3.5-sonnet": {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-opus": {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 15,
        "price_output_token_1M": 75
    },
    "claude-sonnet": {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-haiku": {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 0.25,
        "price_output_token_1M": 1.25
    }
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
