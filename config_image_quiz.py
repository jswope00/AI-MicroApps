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

def prompt_conditionals(prompt, user_input, phase_name=None):
    #TO-DO: This is a hacky way to make prompts conditional that requires the user to know a lot of python and get the phase and field names exactly right. Future task to improve it. 




    return prompt
    
selected_llm = "gpt-3.5-turbo"


LLM_CONFIGURATIONS = {
    "gpt-3.5-turbo": {
        "model": "gpt-3.5-turbo-0125",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.50,
        "price_output_token_1M":1.50
    },
    "gpt-4-turbo": {
        "model": "gpt-4-turbo",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":10,
        "price_output_token_1M":30
    },
    "gpt-4o": {
        "model": "gpt-4o",
        "frequency_penalty": 0,
        "max_tokens": 250,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":5,
        "price_output_token_1M":15
    },
    "gemini-1.0-pro": {
        "model": "gemini-1.0-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.5,
        "price_output_token_1M":1.5
    },
    "gemini-1.5-flash": {
        "model": "gemini-1.5-flash",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.35,
        "price_output_token_1M":1.05
    },
    "gemini-1.5-pro": {
        "model": "gemini-1.5-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":3.5,
        "price_output_token_1M":10.50
    },
    "claude-3.5-sonnet": {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-opus": {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 15,
        "price_output_token_1M": 75
    },
    "claude-sonnet": {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-haiku": {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 0.25,
        "price_output_token_1M": 1.25
    }
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
