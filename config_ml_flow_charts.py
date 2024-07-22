APP_TITLE = "Flow chart Analysis"
APP_INTRO = """This app demonstrates AI microapp image fields."""

APP_HOW_IT_WORKS = """
"""

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You are a proctor for a student taking an quiz. They will answer questions about an image and you will provide feedback and scores. If you are provided a rubric, then you will use it. If you are not provided a rubric, then you won't provide a score. You are precise in reading instructions and providing scores."""


PHASES = {
    "phase1": {
        "name": "Upload and Describe ML Flowchart",
        "fields": {
            "ml_flowchart": {
                "type": "file_uploader",
                "label": "Upload your flowchart of a machine learning process (PNG or JPG format)",
                "value": None,
                "help": "Upload an image file. Supported formats: jpg, jpeg, png"
            }
        },
        "phase_instructions": "Upload an image of your flowchart depicting a machine learning process and describe what it represents, including any specific ML process and main steps involved.",
        "user_prompt": "I have uploaded my ML flowchart",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
            1. Process Clarity:
                2 points - Flowchart clearly represents a specific ML process.
                1 point - Flowchart represents an ML process but lacks some clarity.
                0 points - Flowchart is unclear or doesn't represent an ML process.
            2. Key Steps:
                2 points - Includes at least 5 key steps in the correct order.
                1 point - Includes 3-4 key steps, mostly in the correct order.
                0 points - Includes fewer than 3 key steps or steps are out of order.
        """,
        "minimum_score": 2
    },
    "phase2": {
        "name": "Detail Analysis of ML Process",
        "fields": {
            "data_prep": {
                "type": "text_area",
                "label": "Describe the data preparation step in your flowchart:",
                "value": "In the data preparation step, the flowchart shows data being collected from various sources, cleaned to remove noise and inconsistencies, and then normalized to ensure the model processes it effectively.",
                "placeholder": "Explain how data preparation is represented in your flowchart."
            },
            "model_selection": {
                "type": "text_area",
                "label": "What model or algorithm does your flowchart use?",
                "value": "The model selected in the flowchart is a decision tree algorithm, which is used for classifying the data into different predefined categories based on learned patterns.",
                "placeholder": "Name and describe the model or algorithm featured."
            },
            "evaluation": {
                "type": "text_area",
                "label": "How is the model evaluated according to your flowchart?",
                "value": "The flowchart depicts the evaluation through cross-validation techniques, where the dataset is split into training and validation sets to test the model's accuracy and prevent overfitting.",
                "placeholder": "Describe the evaluation step in your flowchart."
            }
        },
        "phase_instructions": "Provide detailed descriptions of specific steps in your ML process flowchart, focusing on data preparation, model selection, and evaluation.",
        "user_prompt": "Here are the key steps I've identified in my flowchart:\nData Preparation: {data_prep}\nModel Selection: {model_selection}\nEvaluation: {evaluation}",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
            1 point for each correct identification and explanation of a key ML process step:
            - Data Preparation: e.g., cleaning, normalization, feature selection.
            - Model Selection: correctly identifies an ML algorithm appropriate for the process.
            - Evaluation: describes a valid evaluation method (e.g., cross-validation, test set performance).
            0 points for incorrect identifications or explanations.
        """,
        "minimum_score": 2
    },
    "phase3": {
        "name": "Reflection and Questions",
        "fields": {
            "reflection": {
                "type": "text_area",
                "label": "Reflect on your flowchart. What aspects of the ML process did you find challenging to represent? What would you like to improve?",
                "value": "I found it challenging to accurately depict the complexity of model training in the flowchart without making it too cluttered. I would like to improve the visual clarity of this step.",
                "placeholder": "Share your thoughts on the flowchart creation process."
            },
            "student_question": {
                "type": "text_area",
                "label": "Do you have any questions about the ML process you've diagrammed or how to improve your flowchart?",
                "value": "Could you suggest techniques to make the model training step clearer in the flowchart?",
                "placeholder": "Ask any questions you might have about the ML process or improving your flowchart."
            }
        },
        "phase_instructions": "Reflect on the creation of your ML flowchart and ask any questions you have about the process.",
        "user_prompt": "Here's my reflection: {reflection}\n\nAnd here's my question: {student_question}",
        "allow_skip": True,
        "scored_phase": False
    }
}

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
