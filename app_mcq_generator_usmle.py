PUBLISHED = True
APP_URL = "https://mcq-wizard-usmle.streamlit.app"
APP_IMAGE = "mcq_generator_flat.webp"

APP_TITLE = "MCQ Generator (USMLE Style)"
APP_INTRO = """This micro-app allows you to generate clinical vignette (USMLE style) multiple-choice questions quickly and consistently. 
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

SYSTEM_PROMPT = ""

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
            "question_type": {
                "type": "selectbox",
                "label": "Question Type (optional)",
                "options": ["Diagnosis", "Treatment", "Mechanism", "Epidemiology", "Pathophysiology", "Biostatistics"],
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
            "question_level": {
                "label": "Question difficulty level:",
                "type": "selectbox",
                "options": ['Normal', 'Easy', 'Hard'],
                "index": 0,
            },
            "distractors_num": {
                "label": "Number of distractors:",
                "type": "selectbox",
                "options": [1, 2, 3, 4, 5],
                "index": 3,
            },
            "learner_feedback": {
                "type": "checkbox",
                "label": "Include Learner Feedback?",
                "value": True,
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
        "phase_instructions": "",
        "user_prompt": [
            {
            "condition": {},
            "prompt": "I want you to act as an expert medical educator specializing in writing high-quality clinical vignette-style questions for the USMLE Step exams. Please create {questions_num} {question_level} multiple-choice question(s), each with {correct_ans_num} correct answer(s) and {distractors_num} distractors, following these specifications:\n"
            },
            {
                "condition": {"question_type": {"$ne":""}},
                "prompt": "Please create questions based on the following question type: {question_type}\n\n"
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
                "condition": {},
                "prompt": "Distractors should be based on common misconceptions or related conditions.\n\n"
            },
            {
                "condition": {"learning_objective": {"$ne":""}},
                "prompt": "Focus on meeting the following learning objective(s): {learning_objective}\n"
            },
            {
                "condition": {"learner_feedback": True},
                "prompt": "Please provide a feedback section where you Clearly identify the correct answer, Provide a detailed explanation for why the correct answer is correct, and Briefly explain why each distractor is incorrect or less likely. \n\n"
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
                "condition": {},
                "prompt": """When you write clinical vignettes, please include: \n
                - Patient demographics (age, gender, relevant history).\n
                -  Presenting symptoms and clinical findings.\n
                - Pertinent medical history, social history, or family history (if applicable).\n
                - Relevant lab results, imaging findings, or diagnostic tests.\n"""
            },
            {
                "condition": {"output_format": {"$ne":"OLX"}},
                "prompt": """Here is a sample question:
                    A 45-year-old man presents to the emergency department with a 2-day history of severe chest pain radiating to his left arm and jaw. He describes the pain as "crushing" and rates it 8/10 in intensity. He has a history of hypertension and smokes one pack of cigarettes per day. On examination, his blood pressure is 160/90 mmHg, and his heart rate is 110 bpm. An ECG shows ST-segment elevations in leads II, III, and aVF.\n\n

                    Answer Choices:\n
                    A. Acute pericarditis\n
                    B. Non-ST elevation myocardial infarction (NSTEMI)\n
                    C. Pulmonary embolism\n
                    D. ST-elevation myocardial infarction (STEMI)\n
                    E. Stable angina\n\n

                    Correct Answer: D. ST-elevation myocardial infarction (STEMI)\n\n

                    Explanation:\n

                    Correct Answer (D): The patient’s presentation, including acute chest pain radiating to the left arm and jaw, a history of smoking and hypertension, and ECG findings of ST-segment elevation in leads II, III, and aVF, are classic for an inferior STEMI.\n
                    Incorrect Choices:\n
                    A: Acute pericarditis often presents with pleuritic chest pain that improves with leaning forward and diffuse ST elevations. This is inconsistent with this patient's focal ECG changes and presentation.\n
                    B: NSTEMI lacks ST-segment elevations on ECG.\n
                    C: Pulmonary embolism typically presents with dyspnea, tachycardia, and pleuritic chest pain, often accompanied by signs of right heart strain on ECG.\n
                    E: Stable angina is exertional, relieved by rest, and would not cause ST elevations."""
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

PREFERRED_LLM = "gpt-4o"

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
    "page_title": "MCQ Generator (USMLE Style)",
    "page_icon": "️🔤",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
