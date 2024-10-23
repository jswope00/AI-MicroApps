PUBLISHED = True
APP_URL = "https://lo-mapper.streamlit.app"

APP_TITLE = "Learning Objectives Mapper"
APP_INTRO = """This AI-powered Microapp maps content to learning objectives, so educators can quickly remind themselves where in their content they speak to specific learning objectives. 
"""

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """
"""

PHASES = {
    "about": {
        "name": "Learning Objectives",
        "fields": {
        },
        "user_prompt": [
        ]
        "ai_response": True,
        "allow_revisions": True,
        "show_prompt": True,
        "read_only_prompt": False
    }

}
    
PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {"gpt-4o-mini": {
        "family": "openai",
        "model": "gpt-4o-mini",
        "max_tokens": 10000,
        "temperature": 1.0,
        "top_p": 1.0,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "supports_image": False,
        "price_input_token_1M": 0.15,
        "price_output_token_1M": 0.60
    }
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Hope this app saves you some time!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "LO Mapper",
    "page_icon": "️🗺️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
