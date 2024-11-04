PUBLISHED = True
APP_URL = "https://lo-mapper.streamlit.app"
APP_IMAGE = "lo_mapper.webp"

APP_TITLE = "Learning Objectives Mapper"
APP_INTRO = """This AI-powered Microapp maps content to learning objectives, so educators can quickly remind themselves where in their content they speak to specific learning objectives. 
"""

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """
You are an expert instructional designer tasked with aligning course content to specific learning objectives. For each learning objective, identify the most relevant content from the provided materials that will best support achieving that objective. Explain how the chosen content directly contributes to the mastery of the learning objective.
"""

PHASES = {
    "about": {
        "name": "Map Your Learning Objectives to Content",
        "fields": {
        	"learning_objectives": {
                "type": "text_area",
                "height": 200,
                "label": "Please enter your learning objectives, separated by a new line or bullet points/dashes.",
            },
            "content": {
                "type": "text_area",
                "height": 400,
                "label": """Enter your content which you'd like mapped to objectives"""
            },
            "suggestions": {
                "type": "checkbox",
                "label": "Suggest content to fill gaps?"
            }
        },
        "user_prompt": [
            {
            	"condition": {},
            	"prompt": """Please review the content I provide and attempt to map specific sections of my content to learning objectives. 
                An objective can map to zero, one or many pieces of content. Content might also map to more than one objective.
                Please map no more than three pieces of content to an objective. If you find more than three, prioritize the most relevant three.
                """
            },
            {
            	"condition": {"suggestions": True},
            	"prompt": "If a gap is found where a learning objective does not have any relevant content, please suggest some content to fill that gap."
            },
            {
            	"condition": {"suggestions": False},
            	"prompt": "If a gap is found where a learning objective does not have any relevant content, please only flag the gap but don't make any suggestions for how to fill it."
            },
            {
            	"condition": {},
            	"prompt": """Here is the format I'd like your output:
                **[Learning Objective 1]**
                - [One sentence reflecting the relevant content]
                    - [Source text from the content]
                - [One sentence reflecting the relevant content]
                    - [Source text from the content]
                - [Etc, for as much relevent content as there is]
                    - [Source text from the content]

                **[Learning Objective 2]**
                - [One sentence reflecting the relevant content]
                    - [Source text from the content]
                - [One sentence reflecting the relevant content]
                    - [Source text from the content]
                - [Etc, for as much relevent content as there is]
                    - [Source text from the content]

                **[Learning Objective 3]**
                - No content maps to this objective! [use this when you find no mappings]
                
                """
            },
            {
            	"condition": {},
            	"prompt": """Here are my learning objectives:
                {learning_objectives}

                Here is my content:
                {content}
                """
            }
        ],
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
