APP_TITLE = "Zodiac Symbol"
APP_INTRO = """This is a demonstration app that determines a users zodiac symbol based on their birth month and date. 
"""

APP_HOW_IT_WORKS = """
This app collects the name, birth Month, and birth date of the user, and provides them their Zodiac symbol. 
It utilizes the OpenAI and other AI APIs to send a custom prompt to AI with the user's inputs and returns the AI's response. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    
}

SYSTEM_PROMPT = """You are an expert in zodiac symbols. You know the accurate zodiac symbol based on a person's birth month and date, and you """

PHASES = {
    "name": {
        "name": "User Details",
        "fields": {
            "name": {
                "type": "text_input",
                "label": """What is your first name?""",
                "helper": "First name only, please",
                "value": "",
            },
            "system": {
                "type": "selectbox",
                "label": """Astrology System""",
                "options": ["Western","Chinese"],
            },
            "month": {
                "type": "radio",
                "label": """What is your birth month?""",
                "options": ["January","February","March","April","May","June","July","August","September","October","November","December"],
                "showIf": "{system} = \"Western\"",
            },
            "day": {
                "type": "number_input",
                "label": """What is your birth day?""",
                "min_value": 1,
                "max_value":31,
                "showIf": "{system} = \"Western\"",
            },
            "year": {
                "type": "number_input",
                "label": """What is your birth year?""",
                "min_value": 1900,
                "max_value":2020,
                "showIf": "{system} = \"Chinese\"",
            },



        },
        "phase_instructions": "",
        "prompt": {
            "prompt": {
                "prompt": "Give me my Western zodiac. My birth month is {month} and {day}",
                "includeIf": "{system} = \"Western\"",
            },
            "prompt2": {
                "prompt": "Give me my Chinese zodiac. My birth year is {year}",
                "includeIf": "{system} = \"Chinese\"",
            },
        },
        "user_prompt": "My name is {name}. I was born on {month} {day}, {year}. Please provide me my zodiac symbol, and give a short horoscope for the day, according to the {system} astrology system.",
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
        #"read_only_prompt": False
    }


}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
