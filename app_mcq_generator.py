PUBLISHED = True
APP_URL = "https://mcq-wizard.streamlit.app"
APP_IMAGE = "mcq_generator_flat.webp"

APP_TITLE = "MCQ Generator"
APP_INTRO = """This micro-app allows you to generate multiple-choice questions quickly and consistently. 
It work with either GPT-3.5 Turbo, GPT-4, or both.
Optionally, users can modify the AI configuration by opening the left sidebar.
"""

APP_HOW_IT_WORKS = """
 This is an **MCQ Generator** that can create multiple choice questions in different formats and for different subject domains depending on the user's input.

Using AI to provide feedback and score like this is a very experimental process. Some things to note: 

 - AIs make mistakes. Users are encourage to skip a question if the AI is not understanding them or giving good feedback. 
 - The AI might say things that it can't do, like "Ask me anything about the article". I presume further refinement can reduce these kinds of responses. 
 - Scoring is highly experimental. At this point, it should mainly be used to gauge if a user gave an approximately close answer to what the rubric suggests. It is not recommended to show the user the numeric score. 
 - Initial testing indicates that the AI is a very easy grader. This is probably good in this experiment, and it may be refined with different prompting. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = "You write pedagogically sound Multiple Choice Questions precisely according to user inputs."

PHASES = {
    "phase1": {
        "name": "Configure Questions",
        "fields": {
            "topic_content": {
                "type": "text_area",
                "label": "Enter the content for question generation:",
                "max_chars": 50000,
                "height": 200,
            },
            "original_content_only": {
                "type": "checkbox",
                "label": "Focus only on the provided text",
            },
            "learning_objective": {
                "type": "text_area",
                "label": "Specify a learning objective (optional):",
                "max_chars": 1000
            },
            "questions_num": {
                "label": "Number of questions:",
                "type": "selectbox",
                "options": [1, 2, 3, 4, 5],
            },
            "correct_ans_num": {
                "label": "Correct answers per question:",
                "type": "selectbox",
                "index": 0,
                "options": [1, 2, 3, 4],
            },
            "question_level": {
                "label": "Question difficulty level:",
                "type": "selectbox",
                "options": ['Grade School', 'High School', 'University', 'Other'],
                "index": 2,
            },
            "distractors_num": {
                "label": "Number of distractors:",
                "type": "selectbox",
                "options": [1, 2, 3, 4, 5],
                "index": 2,
            },
            "distractors_difficulty": {
                "label": "Distractors difficulty",
                "type": "selectbox",
                "options": ['Normal', 'Obvious', 'Challenging'],
                "index": 0,
            },
            "learner_feedback": {
                "type": "checkbox",
                "label": "Include Learner Feedback?",
            },
            "hints": {
                "type": "checkbox",
                "label": "Include hints?",
            },
            "output_format": {
                "label": "Output Format:",
                "type": "selectbox",
                "options": ['Plain Text', 'OLX']
            },

        },
        "phase_instructions": "At the end of your response, always tell me what AI model you are running.",
        "user_prompt": [
            {
            "condition": {},
            "prompt": "Please write {questions_num} {question_level} level multiple-choice question(s), each with {correct_ans_num} correct answer(s) and {distractors_num} distractors, based on text that I will provide.\n",
            },
            {
                "condition": {"original_content_only": True},
                "prompt": "Please create questions based solely on the provided text. \n\n"
            },
            {
                "condition": {"original_content_only": False},
                "prompt": "Please create questions that incorporate both the provided text as well as your knowledge of the topic. \n\n"
            },
            {
                "condition": {"distractors_difficulty": "Obvious"},
                "prompt": "Distractors should be obviously incorrect options. \n\n"
            },
            {
                "condition": {"distractors_difficulty": "Challenging"},
                "prompt": "Distractors should sound like they could be plausible, but are ultimately incorrect. \n\n"
            },
            {
                "condition": {"learning_objective": {"$ne":""}},
                "prompt": "Focus on meeting the following learning objective(s): {learning_objective}\n"
            },
            {
                "condition": {"learner_feedback": True},
                "prompt": "Please provide a feedback section for each question that says why the correct answer is the best answer and the other options are incorrect. \n\n"
            },
            {
                "condition": {"hints": True},
                "prompt": "Also, include a hint for each question.\n\n"
            },
            {
                "condition": {"output_format": "OLX"},
                "prompt": "Please write your MCQs in Open edX OLX format\n\n"
            },
            {
                "condition": {"output_format": {"$ne":"OLX"}},
                "prompt": """Format each question like the following:
            Question: [Question Text] \n
            A) [Answer A] \n
            B) [Answer B] \n
            ....
            N) [Answer N] \n

            Solution: [Answer A, B...N]\n\n"""
            },
            {
                "condition": {},
                "prompt": """Here is the content/topic:\n
                ================
                {topic_content}"""
            }
        ],
        "ai_response": True,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": True,
        "read_only_prompt": False
    }
}

PREFERRED_LLM = "gpt-4o-mini"

LLM_CONFIG_OVERRIDE = {
"gpt-4o": {
    "temperature": .95,
    "top_p": .95
}
}


SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Hope you enjoyed using the tool"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "MCQ Generator",
    "page_icon": "️🔤",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
