
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
            "audience": {
                "label": "Describe the audience",
                "type": "selectbox",
                "options": ['University', 'High School', 'Grade School']
            },

        },
        "phase_instructions": "",
        "user_prompt": "Please provide feedback for the following question: {question_text}",
        "allow_skip": True,
    }
 
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False