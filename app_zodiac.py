PUBLISHED = True
APP_URL = "https://ai-zodiac.streamlit.app/"
APP_IMAGE = "zodiac_flat.webp"

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
                "value":""
            },
            "name": {
                "type": "text_input",
                "label": "What is your first name?",
                "helper": "First name only, please",
                "value": "John",
                "showIf": {"system": {"$in": ["Western", "Chinese"]}}
            },
            "month": {
                "type": "radio",
                "label": "What is your birth month?",
                "options": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                "showIf": {"$and": [{"system": "Western"}, {"name": {"$ne": ""}}]}
            },
            "day": {
                "type": "number_input",
                "label": "What is your birth day?",
                "min_value": 1,
                "max_value": 31,
                "showIf": {"$and": [{"system": "Western"}, {"name": {"$ne": ""}}]}
            },
            "year": {
                "type": "number_input",
                "label": "What is your birth year?",
                "min_value": 1900,
                "max_value": 2020,
                "showIf": {"$and":[{"system": {"$in": ["Western", "Chinese"]}},{"name": {"$ne": ""}}]}
            }
        },
        "phase_instructions": "Please fill in your details to determine your zodiac symbol.",
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
    },
    "phase2": {
        "name": "Zodiac Interpretation",
        "fields": {
            "interested_in_traits": {
                "type": "radio",
                "label": "Are you interested in learning about your personality traits based on your zodiac?",
                "options": ["Yes", "No"]
            },
            "interested_in_compatibility": {
                "type": "radio",
                "label": "Would you like to know about zodiac compatibility?",
                "options": ["Yes", "No"]
            }
        },
        "phase_instructions": "Let's dive deeper into your zodiac interpretation.",
        "user_prompt": [
            {
                "condition": {"$and": [
                    {"interested_in_traits": "Yes"},
                    {"interested_in_compatibility": "Yes"}
                ]},
                "prompt": """I'm interested in learning about both my personality traits and compatibility with other zodiac signs based on my {system} zodiac. Please provide detailed insights."""
            },
            {
                "condition": {"$and": [
                    {"interested_in_traits": "Yes"},
                    {"interested_in_compatibility": "No"}
                ]},
                "prompt": """Please provide me with an interpretation of my personality traits based on my {system} zodiac sign."""
            },
            {
                "condition": {"$and": [
                    {"interested_in_traits": "No"},
                    {"interested_in_compatibility": "Yes"}
                ]},
                "prompt": """I'd like to know more about my compatibility with other zodiac signs based on my {system} zodiac sign."""
            },
{
                "condition": {"$and": [
                    {"interested_in_traits": "No"},
                    {"interested_in_compatibility": "No"}
                ]},
                "prompt": """I'd like to know more about my zodiac in general"""
            }
        ],
        "show_prompt": True,
        "allow_skip": True
    }
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Zodiac Predictor",
    "page_icon": "🌌",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())