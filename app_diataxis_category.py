PUBLISHED = False

APP_TITLE = "Diataxis Categorizer"
APP_INTRO = """This AI-powered Microapp analyzes content and categorizes it according to the Diataxis framework. If it is unsure, it provides a percentage probability of multiple categories.  
"""

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """
You are an expert in the diataxis framework and technical documentation. You analyze provided documentation and provide a category or possible categories for diataxis. 
"""

PHASES = {
    "about": {
        "name": "Categorize your Content",
        "fields": {
            "content": {
                "type": "text_area",
                "height": 400,
                "label": """Enter your content which you'd like categorized"""
            }
        },
        "user_prompt": [
            {
            	"condition": {},
            	"prompt": """Please review the content I provide and attempt categorize it according to the diataxis framework, along with a percentage certainty. Here is the terminology I use for Diataxis:

                ## How-to
How-to topics provide direct and easy-to-follow instructions to accomplish specific goals. For example, topics provide the steps to create a new course subsection and to schedule a course.

                ## Quickstart
Quickstart topics may seem similar to How-Tos but have a different focus. Quickstarts are specifically built for beginners and are meant to help them gain experience with the product. For example taking a course through the entire course lifecycle, even if there is no content, and it’s not exactly how you would do it with a real course, gives a beginner a meaningful experience that helps them better navigate the product.

                ## Reference
Reference topics provide details about a function or feature of the Open edX platform. For example there are many details about course subsections such as the different publication states, grading configuration, and visibility that are not included in the how-to topic Create a Subsection but are fully described in the reference topic Course Subsections. These two topics are linked in See Also sections.

                ## Concept
Concept topics provide best practices or other guidelines for using the Open edX platform. For example, the topics Crafting Effective Learning Objectives and Aligning End-of-Module Assessments to Learning Objectives are meant to provide guidelines for educators.

Simply output the category(s) and percent certainty. For a percentage certainty, include the percentage certainty in parenthesese (). For example, if you are completely certain, this is an example of the format: 

How-To (100%)

If you might be unsure, then the format could be something like these: 

Concept (60%)
Reference (40%)

Quick-Start (90%)
How-To (10%)

Here is my content:
{content}
                
                """
            },
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
