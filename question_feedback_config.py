
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

SYSTEM_INSTRUCTIONS = "You provide pedagogically sound feedback for questions that lack them. Feedback should explain why the correct answer is correct, and provide very brief explanation for why the distractors are incorrect."

PHASES = {
    "phase1": {
        "name": "Feedback",
        "fields": {
                "welcome": {
                "type": "text_area",
                "label": "Question and answer Text:",
                "height": 200,
                "placeholder": "Use the following format, where correct answer(s) are indicated by X:\n\nWhat color is the sky?\n\n( ) Red\n(x) Blue\n( ) Green\n"
            },
            "data": {
                "type": "text_area",
                "label": "Enter the source material",
                "height": 200,
                "placeholder": "",
            },
            "audience": {
                "label": "Describe the audience",
                "type": "selectbox",
                "options": ['University', 'High School', 'Grade School']
            },

        },
        "phase_instructions": "",
        "user_prompt": "Please provide feedback for the following question: {question}",
        "allow_skip": True,
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



