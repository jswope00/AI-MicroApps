APP_URL = "/"

PUBLISHED = False

APP_TITLE = "AI Rubric Evaluation"

APP_INTRO = """
This app evaluates AI's scoring consistency using a custom rubric and compares it to a human-provided score.
"""

APP_HOW_IT_WORKS = """
The app allows you to input a question, a sample answer, a rubric for evaluation, and a human-provided score.
The AI will evaluate the answer based on the rubric multiple times, and you'll see a comparison of the AI's performance
against the human score.
"""

SYSTEM_PROMPT = "You are an AI assistant who evaluates the student's answer"

# Externalize RUBRIC_EVALUATION as a parameter
RUBRIC_EVALUATION_ENABLED = True

NUM_AI_RUNS = 5

PHASES = {
    "phase1": {
        "name": "ShakespeareDramaEvaluation",
        "fields": {
            "question": {
                "type": "text_input",
                "label": "Enter the question",
                "value": "What are the hallmark elements of a Shakespeare drama?"
            },
            "sample_answer": {
                "type": "text_area",
                "label": "Enter the sample answer",
                "value": "Shakespearean dramas involve weddings and a tragedy at the end."
            }
        },
        "phase_instructions": """Provide brief feedback for the student""",
        "user_prompt": """{question}, {sample_answer}""",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 0,
        "human_score":4,
        "rubric": """
        1. Tragedy Element
            3 points - Clearly identifies tragedy as a hallmark element and provides examples or context.
            2 points - Mentions tragedy as an element but without much detail or context.
            1 point - Mentions tragedy, but the connection to Shakespeare's hallmark is vague.
            0 points - Does not mention tragedy.
        2. Comedy Element
            3 points - Clearly identifies comedy as a hallmark element and provides examples or context.
            2 points - Mentions comedy as an element but without much detail or context.
            1 point - Mentions comedy, but the connection to Shakespeare's hallmark is vague.
            0 points - Does not mention comedy.
        """,
        "allow_revisions": False,
        "allow_skip": False,
        "show_prompt": True,
        "read_only_prompt": False
    }
}


PREFERRED_LLM = "gpt-4o-mini"

LLM_CONFIG_OVERRIDE = {
    "gpt-4o-mini": {
        "family": "openai",
        "model": "gpt-4o-mini",
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }
}

COMPLETION_MESSAGE = "Evaluation Complete!"
COMPLETION_CELEBRATION = False

PAGE_CONFIG = {
    "page_title": "AI Rubric Evaluation",
    "page_icon": "🤖",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

RAG_IMPLEMENTATION = True
SOURCE_DOCUMENT = "sample.pdf"

from core_logic.main import main

if __name__ == "__main__":
    main(config=globals())  # Execute your main function




