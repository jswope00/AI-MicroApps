PUBLISHED = True
APP_URL = "https://question-feedback.streamlit.app"
APP_IMAGE = "question_feedback_flat.webp"

APP_TITLE = "Question Feedback"
APP_INTRO = """This app takes existing questions and provides pedogically sound feedback that explains the correct and incorrect answer(s). Immediate feedback is one of the most powerful tools that influences student comprehension. 
"""

APP_HOW_IT_WORKS = """

This app can:

1. provide feedback for a question when provided the question, correct answer(s) and incorrect answer(s)
2. Incorporate course knowledge if provided. 
3. Consider the question format if provided. 

 """

COMPLETION_MESSAGE = "Done! Refresh the page to try again. "
COMPLETION_CELEBRATION = False

SCORING_DEBUG_MODE = True

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = "You provide pedagogically sound feedback for questions that lack them. Feedback should explain why the correct answer is correct, and provide very brief explanation for why the distractors are incorrect."

PHASES = {
    "phase1": {
        "name": "Feedback",
        "fields": {
            "question_text": {
                "type": "text_area",
                "label": "Question and answer Text:",
                "height": 200,
                "placeholder": "Use the following format, where correct answer(s) are indicated by X:\n\nWhat color is the sky?\n\n( ) Red\n(x) Blue\n( ) Green\n"
            },
            "source_material": {
                "type": "text_area",
                "label": "Enter the source material",
                "height": 200,
                "placeholder": "",
            },
            "hints": {
                "type": "checkbox",
                "label": "Provide Hints?",
                "value": False,
            },
            "num_hints": {
                "type": "slider",
                "label": "Number of Hints",
                "min_value": 1,
                "max_value": 4,
                "showIf": {"hints": True}
            }
        },
        "phase_instructions": "",
        "user_prompt": "",
        "show_prompt": True,
        "read_only_prompt": False,
        "user_prompt": [
            {
                "condition": {},
                "prompt": "Please provide feedback"
            },
            {
                "condition": {"hints": True},
                "prompt": "and {num_hints} hints"
            },
            {
                "condition": {},
                "prompt": "for the following questions(s): \n {question_text}"
            },
            {
                "condition": {},
                "prompt": "Adjust your tone based on the tone of the question text."
            },
            {
                "condition": {},
                "prompt": """If provided, please consider the source material in your hints and feedback. If no source material is provided, ignore this: 
Source Material:
{source_material}
                """,
            },
        ]

    }



}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Immediate feedback is great for students!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Question Feedback",
    "page_icon": "️✅",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())

