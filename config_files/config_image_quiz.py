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
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Wrist_and_hand_deeper_palmar_dissection-numbers.svg/809px-Wrist_and_hand_deeper_palmar_dissection-numbers.svg.png",
                "caption": "An diagram of a hand with indicators but no labels",
            },
            "identify": {
                "type": "text_input",
                "label": """What is this a picture of?""",
                "value": "It is an unlabeled diagram of a hand",
            }
        },
        "no_submission": False,
        "phase_instructions": "The user will upload an image. Then they will describe the image. They should mention that the image is of a hand. ",
        "user_prompt": "{identify}",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
                1. Hand
                    1 point - The user identifies that the image is of a hand.
                    0 points - The user identies the image as something other than a hand.
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

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
