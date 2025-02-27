PUBLISHED = True
APP_URL = "https://mcq-svm.streamlit.app"
APP_IMAGE = "mcq_generator_flat.webp"

APP_TITLE = "MCQ Generator (SVM)"
APP_INTRO = """This micro-app allows you to generate multiple-choice questions quickly and consistently. """

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
            "topic": {
                "type": "text_input",
                "label": "Enter the topic for question generation:"
            },
            "learning_objective": {
                "type": "text_area",
                "label": "Specify an ILO (optional):",
                "max_chars": 1000
            },
            "question_type": {
                "type": "radio",
                "label": "Question Type",
                "options": ["Pre-Work", "Formative", "Summative"],
                "index": 0,
            },
            "topic_content": {
                "type": "text_area",
                "label": "Enter the content for question generation:",
                "max_chars": 50000,
                "height": 200,
            },
            "question_style": {
                "type": "selectbox",
                "label": "Question Type",
                "options": ["NAVLE", "Standard" ],
                "index": 0,
            },
            "questions_num": {
                "label": "Number of questions:",
                "type": "selectbox",
                "options": [1, 2, 3, 4, 5],
            },
            "student_level": {
                "label": "Student level:",
                "type": "selectbox",
                "options": ['Pre-Clinical', 'Clinical'],
                "index": 0,
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
            "knowledge_level": {
                "label": "Focus on the following knowledge level (optional):",
                "type": "selectbox",
                "options": ['Any', 'Knowledge', 'Comprehension', 'Application', 'Analysis', 'Synthesis', 'Evaluation'],
            },
            "relevance": {
                "label": "Relevance:",
                "type": "radio",
                "options": ['Essential', 'Important', 'Nice to know'],
            },
            "additional_instructions": {
                "type": "text_area",
                "label": "Enter any additional instructions or customizations:",
                "max_chars": 1000,
                "height": 200,
            }

        },
        "phase_instructions": "",
        "user_prompt": [
            {
            "condition": {},
            "prompt": """You are an expert veterinary educator tasked with creating high-quality multiple-choice questions (MCQs) for veterinary school students. Your questions should be clear, challenging, and educational. Use clinical language and terminology appropriate for {student_level} veterinary students.
            Please create {questions_num} {question_level} multiple-choice question(s), each with {correct_ans_num} correct answer(s) and {distractors_num} distractors, following these specifications:\n
            """
            },
            {
                "condition": {"knowledge_level": {"$ne":"Any"}},
                "prompt": "Focus on the following knowledge level: {knowledge_level}\n\n"
            },
            {
                "condition": {"question_style": "NAVLE"},
                "prompt": """Questions should be in the format of NAVLE questions.\n\n- Focus on complex decision-making and application of clinical knowledge.\n - Include Patient demographics (age, gender, relevant history).\n- Include Presenting symptoms and clinical findings.\n- Pertinent medical history, social history, or family history (if applicable).\n- Include Relevant lab results, imaging findings, or diagnostic tests.\n""",
            },
            {
                "condition": {},
                "prompt": "Distractors should be based on common misconceptions or related conditions. All distractors should be within 1 or 2 words of the same length. \n\n"
            },
            {
                "condition": {"learning_objective": {"$ne":""}},
                "prompt": "Focus on meeting the following learning objective(s): {learning_objective}\n"
            },
            {
                "condition": {},
                "prompt": "Please provide a feedback & rationale section where you clearly identify the correct answer, Provide a detailed explanation for why the correct answer is correct, and Briefly explain why each distractor is incorrect or less likely. \n\n"
            },

            {
                "condition": {"question_style": "Standard"},
                "prompt": """Format each question like the following:
            Question: [Question Text] \n
            A) [Answer A] \n
            B) [Answer B] \n
            ....
            N) [Answer N] \n

            Solution: [Answer A, B...N]\n\n
                """
            },
            {
                "condition": {"question_style": "NAVLE"},
                "prompt": """Here is a sample question:
     A 5-year-old spayed female Labrador retriever presents with acute onset of vomiting, lethargy, and anorexia. The owner reports that the dog had access to a garden containing numerous rodenticides. On physical examination, the dog is tachycardic and has pale mucous membranes. Which of the following is the most appropriate initial diagnostic test?
     
     A. Abdominal radiography  
     B. Complete blood count (CBC)  
     C. Coagulation profile  
     D. Serum biochemistry panel
     E. None of the above

     *Solution:* C
     
     *Explanation:*  
     The clinical scenario raises suspicion for rodenticide poisoning, which commonly leads to coagulopathies. Therefore, a coagulation profile (option C) is the most appropriate initial test to assess for bleeding disorders. Options A, B, and D, while useful in other contexts, do not directly address the suspected underlying coagulopathy.
"""
            },
            {
                "condition": {"additional_instructions": {"$ne":""}},
                "prompt": "Additionally, follow these additional instructions: {additional_instructions}\n"
            },
            {
                "condition": {},
                "prompt": """Here is the content/topic:\n
                ================
                topic: {topic}
                {topic_content}"""
            },
            {
                "condition": {},
                "prompt": """I'm going to copy and paste your response into a strictly formatted templated, so please format your response as follows. If I have left a value blank, then please leave it blank. 
                
                **Topic**: {topic}
                **ILO**: {learning_objective}
                **Question Type**: {question_type}
                **Bloom's Taxonomy Level**: {knowledge_level}
                **Difficulty Level**: {question_level}
                **Relevance**: {relevance}

                **Question Stem**
                [Write the question stem here]

                **Answer Options**
                [Write the answer options here]

                **Correct Answer**
                [Write the correct answer here]

                **Feedback & Rationale**
                [Write the explanation here]
                """

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
    "top_p": .95,
    "max_tokens": 10000,
}
}


SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Hope you enjoyed using the tool"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "MCQ Generator (SVM Style)",
    "page_icon": "️🔤",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

USE_SQL = False
USE_GSHEETS = False

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
