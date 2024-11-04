PUBLISHED = True
APP_URL = "https://lo-analyst.streamlit.app"
APP_IMAGE = "lo_analyst_flat.webp"

APP_TITLE = "Learning Objective Analyst"
APP_INTRO = """
This app uses AI to analyze a single or a set of learning objectives and return feedback on how to improve the objective. Specifically, this app measures how SMART (Specific, Measureable, Actionable, Realistic, Time-Bound) the objectives are.
"""

APP_HOW_IT_WORKS = """
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You analyze learning objectives and provide feedback on how to make those objectives "SMART"er (Specific, Measureable, Achievable, Result-oriented, and Time-Bound.) You provide feedback to the user based on those five dimensions. You do not provide feedback based on criteria outside of those dimensions unless explicitly asked. You are matter-of-fact and straightforward, unless the learning objectives meets all dimensions well. If the learning objective meets all objectives well, then you have an encouraging tone."""

PHASES = {
    "learning_objectives": {
        "name": "Provide your Learning Objectives",
        "fields": {
            "learning_objectives": {
                "type": "text_area",
                "height": 200,
                "label": """Please provide your learning objective(s) for analysis:""",
                "value": "",
                "helper": "Please separate learning objectives with line breaks."
            }
        },
        "phase_instructions": """First, determine how many learning objectives the user has provided (the user has been asked to separate learning objectives by line breaks, but they might not have followed directions and that is OK). 
            Then, for each learning objective, provide feedback on whether it is 
                1. Specific
                2. Measureable
                3. Achievable
                4. Result-Oriented
                5. Time-Bound
            Good learning objectives avoid avoid vague terms like “understand,” “learn,” or “know” because there is no metric for whether learning has occurred or not. Instead, they should use actionable verbs, like those from Bloom's Taxonomy.
            Here are some good, SMART learning objectives:
            - By the end of this unit, students will be able to describe three causes of World War II.
            - By the end of this module, employees will be able to locate the fire escape on each floor.

            Here are some poor ones:
            - By the end of this lesson, students will understand why World War II started (this objective is not specific or measureable)
            - Employees will know what to do in case of fire. (This is not time-bound, measureable, or specific. It may not be achievable if there is a larger scope of what to do in case of fire than can be covered in the lesson.)

            Finally, provide a suggestion on how to rewrite the objective so that it is SMART and includes a verb from Bloom's taxonomy. 
            - """,
        "user_prompt": "Here is/are my learning objective(s): {learning_objectives}",
        "allow_skip": False,

}
}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "I hope this helps improve your learning objectives!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "LO Analyst",
    "page_icon": "️🔹",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())