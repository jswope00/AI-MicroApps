
APP_TITLE = "Find the Incorrect Fact"
APP_INTRO = """In this demonstration, the AI will generate mostly factual information about a topic, with one incorrect fact. It is your job to find the incorrect fact. 
"""

APP_HOW_IT_WORKS = ""

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = ""

PHASES = {
    "phase1": {
        "name": "Choose a Topic",
        "fields": {
                "welcome": {
                "type": "markdown",
                "body": "Welcome! Enter a topic to get started.",
                "unsafe_allow_html": True
            },
            "name_hard_code": {
                "type": "text_input",
                "label": "Choose your topic:",
                "value": "Strep Throat"
            },
        },
        "phase_instructions": "",
        "user_prompt": "Please generate two paragraphs of information about the following topic: {name_hard_code}. Your information should all be factual, except you should sneak one incorrect fact in there that sounds plausible but is in fact incorrect. Do not tell me what the incorrect fact is. ",
        "allow_skip": False,
        "scored_phase": False,
    },
    "phase2": {
        "name": "Find the Incorrect Fact.",
        "fields": {
            "incorrect_fact": {
                "type": "text_input",
                "label": "Which fact is incorrect?",
            }
        },
        "phase_instructions": "The user will provide you the incorrect fact from your last message. Assess if they have found the incorrect fact. If they have found the incorrect fact, tell them they are correct and tell them why the fact is wrong. If the user has not identified the incorrect fact, ask them to try again.",
        "user_prompt": "{incorrect_fact}",
        "scored_phase": False,
        "allow_skip": True,
        "scored_phase": True,
        "allow_revisions": True,
        "max_revisions": 4,
        "rubric": """
            1. Correct Identification
                1 points - The user has correctly identified the incorrect fact. 
                0 points - The user has not correctly identified the incorrect fact. 
        """,
        "minimum_score": 1,
    }
 
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}


SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
