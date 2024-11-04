PUBLISHED = True
APP_URL = "https://image-quiz.streamlit.app"
APP_IMAGE = "image_quiz_flat.webp"

APP_TITLE = "Image Demonstration"
APP_INTRO = """This app demonstrates AI microapp image fields. An instructor can share an image with the student and have the student answer questions about it. The AI will provide instructor-guided feedback.
"""

APP_HOW_IT_WORKS = """
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You are a proctor for a student taking an image quiz. They will answer questions about an image and you will provide feedback and scores. If you are provided a rubric, then you will use it. If you are not provided a rubric, then you won't provide a score. You are precise in reading instructions and providing scores."""

PHASES = {
    "phase0": {
        "name": "Image",
        "fields": {
            "name": {
                "type": "image",
                "image": "https://appsforeducation.s3.amazonaws.com/cholesterol.jpg",
                "caption": "A series of artery cutaways showing a progression of some kind of blockage.",
            },
            "identify": {
                "type": "text_area",
                "height": 125,
                "label": """What is occuring in the progression shown in the image? Make sure to mention the specific condition, the yellow substance, and the risks of this condition.""",
                "value": "The image depicts the progression of atherosclerosis, a condition in which plaque builds up inside the arteries. Atherosclerosis restricts blood flow and leads to increased risk of blod clots, heart attacks, and stroke. ",
            }
        },
        "no_submission": False,
        # "phase_instructions": "The user will upload an image. Then they will describe the image. They should mention that the image is of a hand. ",
        "user_prompt": "{identify}",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
                1. atherosclerosis
                    1 point - The user mentions atherosclerosis
                    0 points - The user does not mention atherosclerosis
                2. cholesterol/plaque
                    1 point - The user correctly identifies that the image shows a plaque or cholesterol buildup. Either term is acceptable. 
                    0 points - THe user does not mention plaque or cholesterol. 
                3. risks
                    3 point - The user mentions all relevant points: This condition restricts blood flow and increases risk of heart attack, stroke, and other cardiovascular conditions.
                    2 point - The user mentions some of the relevant points: This condition restricts blood flow and increases risk of heart attack, stroke, and other cardiovascular conditions.
                    1 points - THe user mentions at least one of the relevant points: This condition restricts blood flow and increases risk of heart attack, stroke, and other cardiovascular conditions.
                    0 points - The user fails to mention any risks. 
            """,
        "minimum_score": 1
    },
    "phase1": {
        "name": "Ask Questions about the image",
        "fields": {
            "question": {
                "type": "text_area",
                "label": """Do you have questions about the image?""",
                "value": "",
            }

        },
        "phase_instructions": "The user will ask a question about the image. Please respond to their question.",
        "user_prompt": "{question}",
        "allow_skip": True,
    }

}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Image Quiz",
    "page_icon": "️🖼️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())