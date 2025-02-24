PUBLISHED = True
APP_URL = "https://microapp-demo1.streamlit.app"
APP_IMAGE = "demo1_flat.webp"

APP_TITLE = "MicroApp Demo App #1"
APP_INTRO = """This app demonstrates all the fields that are available to a micro-app. It can be used to understand what kinds of inputs a micro-app can ask for, and how to configure those fields. 
"""

APP_HOW_IT_WORKS = """
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You provide brief 1-2 sentence answers to the instructions you are provided. You never ask questions in your responses. """

PHASES = {
    "phase1": {
        "name": "Text Input",
        "fields": {
            "name": {
                "type": "text_input",
                "label": """What is your first name?""",
                "value": "John",
            }

        },
        "phase_instructions": "The user will provide their name. Please welcome them by name. ",
        "user_prompt": "{name}",
        "allow_skip": True,
    },
    "phase2": {
        "name": "Text Area",
        "fields": {
            "hobbies": {
                "type": "text_area",
                "height": 200,
                "label": """What are your favorite hobbies?""",
                "value": "Golf, Crossword Puzzles, Fantasy Football",
            }
        },
        "phase_instructions": "The user will introduce their hobbies now, and I'll say what I like about one of those hobbies. ",
        "user_prompt": "{hobbies}",
        "allow_skip": True,
  
    },
    "phase3": {
        "name": "Chat Area",
        "fields": {
            "chat": {
                "type": "chat_input",
                "max_messages": 3,
                "placeholder": "What is your name?",
                "initial_assistant_message": "Hello, I'm a chatbot with a name. You have to determine my name."
            }
        },
        "allow_skip": True,
        "ai_response": True,
        "phase_instructions": "Your name is Bottina. You will tell the user your name if they ask.",
        "user_prompt": "Please provide feedback on whether or not I discovered that the bot's name is Bottina in this chat: \n\n{chat}",
        "scored_phase": True,
        "rubric": """
        1. Name:
        2 points - The user determined that the bot's name is Bottina.
        0 points - The user has NOT determined that the bot's name is Bottina.
        """,
        "minimum_score": 0,
        "show_prompt": False,
    },
    "phase4": {
        "name": "Radio Select",
        "fields": {
            "pluto": {
                "type": "radio",
                "options": ['Yes!', 'No', 'It is whatever NASA tells me it is.'],
                "label": "Is Pluto a planet?",
            }
        },
        "phase_instructions": "The user has been asked 'Is pluto a planet?' and will give their response. Comment on their response",
        "user_prompt": "{pluto}",
        "allow_skip": True,
    },
    "phase5": {
        "name": "Dropdown Select",
        "fields": {
            "tech": {
                "type": "selectbox",
                "options": ['Mac', 'PC', 'Linux!', 'Stone Tablet'],
                "label": "Mac or PC?",
            }
        },
        "phase_instructions": "The user will tell you whether they prefer Mac, PC, Linux or provide a flippant answer about their choice of technology. Tell them a joke about whatever their choice is.",
        "user_prompt": "{tech}",
        "allow_skip": True,
    },
    "phase6": {
        "name": "Checkbox",
        "fields": {
            "check_me": {
                "type": "checkbox",
                "label": "Check this box!",
            }
        },
        "phase_instructions": "The user will tell you if they have pets or not. Comment on it.",
        "ai_response": False,
        "custom_response": "Thanks!",
        "allow_skip": True,
    },
    "phase7": {
        "name": "age",
        "fields": {
            "age": {
                "type": "slider",
                "min_value": 5,
                "max_value": 100,
                "label": "How old are you?",
            }
        },
        "phase_instructions": "The user will provide their age. Say something encouraging about their age.",
        "user_prompt": "{age}",
        "allow_skip": True,
    },
    "phase8": {
        "name": "mars",
        "fields": {
            "mars": {
                "type": "number_input",
                "step": 1,
                "label": "In what year do you think the first human will reach step foot on Mars?",
            }
        },
        "phase_instructions": "The user will predice what year the first person will step foot on Mars. React to their answer. If their answer is non-sensical, provide a sarcastic comment.",
        "user_prompt": "{mars}",
        "allow_skip": True,
    }

}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {
    "max_tokens": 8000,
    "temperature": 1.0
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Demo 1",
    "page_icon": "️🖥️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

USE_SQL = True
USE_GSHEETS = True
GSHEETS_URL_OVERRIDE = "https://docs.google.com/spreadsheets/d/1TGCZfdbBUbegi2Gi91_VmtazkpZGOS2g16qquX6pLp0/edit?gid=0#gid=0"
GSHEETS_WORKSHEET_OVERRIDE = "Sheet1"

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())