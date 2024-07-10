
APP_TITLE = "Guided Critical Analysis"
APP_INTRO = """In this guided case study, we'll both read the same case study. Then, you'll be guided through an analysis of the paper. Let's begin by reading the paper!

This is a **DEMO**, so sample answers are pre-filled and the article is one that is highly familiar to people.
"""

APP_HOW_IT_WORKS = """
 This is an **AI-Tutored Rubric exercise** that acts as a tutor guiding a student through a shared asset, like an article. It uses the OpenAI Assistants API with GPT-4. The **questions and rubric** are defined by a **faculty**. The **feedback and the score** are generarated by the **AI**. 

It can:

1. provide feedback on a student's answers to questions about an asset
2. roughly "score" a student to determine if they can move on to the next section.  

Scoring is based on a faculty-defined rubric on the backend. These rubrics can be simple (i.e. "full points if the student gives a thoughtful answer") or specific with different criteria and point thresholds. The faculty also defines a minimum pass threshold for each question. The threshold could be as low as zero points to pass any answer, or it could be higher. 

Using AI to provide feedback and score like this is a very experimental process. Some things to note: 

 - AIs make mistakes. Users are encourage to skip a question if the AI is not understanding them or giving good feedback. 
 - The AI might say things that it can't do, like "Ask me anything about the article". I presume further refinement can reduce these kinds of responses. 
 - Scoring is highly experimental. At this point, it should mainly be used to gauge if a user gave an approximately close answer to what the rubric suggests. It is not recommended to show the user the numeric score. 
 - Initial testing indicates that the AI is a very easy grader. This is probably good in this experiment, and it may be refined with different prompting. 
 """

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

SCORING_DEBUG_MODE = True

SHARED_ASSET = {
}

HTML_BUTTON = {
    "url":"http://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf",
    "button_text":"Read PDF"
}

SYSTEM_INSTRUCTIONS = "You are a medical assistant that follows instructions."

PHASES = {
    "phase1": {
        "name": "Choose a Disease",
        "fields": {
                "welcome": {
                "type": "markdown",
                "body": "Welcome! Enter a disease to get started.",
                "unsafe_allow_html": True
            },
            "name_hard_code": {
                "type": "text_input",
                "label": "Choose your disease:",
                "value": "Strep Throat"
            },
        },
        "phase_instructions": "The user will provide you with the name of a disease. If the user enters a valid disease, then generate a two paragraph patient guide for understanding that disease. Your guide should be mostly factual, but include one sentence with an incorrect fact. If the user does not enter a valid disease, ask them to try again with a valid disease.",
        "user_prompt": "Strep Throat",
        "allow_skip": False,
        "scored_phase": True,
        "rubric": """
            1. Valid Disease
                1 points - The user has input a valid disease
                0 points - The user has not input a valid disease
        """,
        "minimum_score": 1,
    },
    "phase2": {
        "name": "Find the Incorrect Fact.",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "Which fact is incorrect?",
            }
        },
        "phase_instructions": "The user will provide you the incorrect fact from your last message. Assess if they have found the incorrect fact. If they have found the incorrect fact, tell them they are correct and tell them why the fact is wrong. If the user has not identified the incorrect fact, ask them to try again.",
        "user_prompt": "My name is {name} and here my background: {background} ",
        "scored_phase": False,
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
            1. Correct Identification
                1 points - The user has correctly identified the incorrect fact. 
                0 points - The user has not correctly identified the incorrect fact. 
        """,
        "minimum_score": 1,
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



