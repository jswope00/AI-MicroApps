PUBLISHED = True
APP_URL = "https://pm-interview.streamlit.app"
APP_IMAGE = "interview_practice_flat.webp"

APP_TITLE = "Sample Interview: Product Manager"
APP_INTRO = """This app asks three standard (fixed) interview questions and provides feedback for the users responses to those questions. It is 
"""


SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """
You play the role of a mock interviewer. The user will answer interview questions and you'll provide feedback based on specific criteria. Please align your feedback to the criteria. """


PHASES = {
    "phase1": {
        "name": "Product Manager Interview - Question 1",
        "fields": {
            "question1_response": {
                "type": "text_area",
                "label": "Describe a product you have managed. What was your role and the outcome?",
                "height": 200,
                "value": "I managed a mobile app project for a local restaurant. My role involved overseeing the development process and ensuring that the team met the deadlines. We successfully launched the app, although we faced some initial challenges with user engagement which we addressed through updates."
            }
        },
        "user_prompt": """The candidate answered the first interview question: 'Describe a product you have managed. What was your role and the outcome?'. 
        You will provide feedback on: 
         - The clarity of their response.
          - The description of their roles and responsibilities
          - The clear communication of outcomes. 
        Here is the user's answer: 
        {question1_response}. """,
        "ai_response": True,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": False,
        "rubric": """
            1. Clarity of Response
                3 points - Very clear and easy to understand.
                2 points - Somewhat clear, with minor ambiguities.
                1 point - Unclear and difficult to follow.
            2. Role and Responsibilities
                4 points - Specific and detailed description of responsibilities.
                3 points - General description with some specific details.
                2 points - Vague description of responsibilities.
                1 point - Responsibilities not clearly mentioned.
            3. Outcome Communication
                3 points - Outcome is clearly and effectively communicated.
                2 points - Outcome is mentioned but lacks detail.
                1 point - Outcome is poorly communicated or missing.
        """,
        "scored_phase": True,
        "minimum_score": 5,
    },
    "phase2": {
        "name": "Product Manager Interview - Question 2",
        "fields": {
            "question2_response": {
                "type": "text_area",
                "label": "How do you prioritize different product features?",
                "height": 200,
                "value": "I prioritize product features based on their impact and feasibility. I usually create a simple matrix to compare the features. Features that have high impact and are easy to implement usually get prioritized. However, I try to also balance user requests and stakeholder inputs."
            }
        },
        "user_prompt": """The candidate answered the second interview question: 'How do you prioritize different product features?'. 
        You will provide feedback on: 
         - Their understanding of prioritization.
          - Their communication of their methodology
          - The effectiveness of their practical examples
        Here is the user's answer: 
        {question2_response}. """,
        "ai_response": True,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": False,
        "rubric": """
            1. Understanding of Prioritization
                3 points - Excellent understanding.
                2 points - Good understanding with minor gaps.
                1 point - Poor understanding.
            2. Methodology
                4 points - Clearly articulated and structured method.
                3 points - Generally described method with some structure.
                2 points - Vague method lacking structure.
                1 point - No method or structure mentioned.
            3. Practical Examples
                3 points - Relevant and effective examples provided.
                2 points - Somewhat relevant examples.
                1 point - Examples are missing or irrelevant.
        """,
        "scored_phase": True,
        "minimum_score": 5,
    },
    "phase3": {
        "name": "Product Manager Interview - Question 3",
        "fields": {
            "question3_response": {
                "type": "text_area",
                "label": "What is your approach to handling product feedback and improving the user experience?",
                "height": 200,
                "value": "I gather feedback from multiple sources including surveys, app reviews, and direct user interviews. After collecting feedback, I analyze the data to identify common trends and issues. I prioritize feedback that affects user experience the most. Regular updates and testing are my main strategies for improvement."
            }
        },
        "user_prompt": """The candidate answered the second interview question: 'What is your approach to handling product feedback and improving the user experience?'. 
        You will provide feedback on: 
         - Their handling of feedback
          - Their user experience improvement
          - Examples of real-world applications
        Here is the user's answer: 
        {question3_response}. """,
        "ai_response": True,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": False,
        "rubric": """
            1. Feedback Handling
                3 points - Very effectively.
                2 points - Somewhat effectively, with room for improvement.
                1 point - Ineffectively.
            2. User Experience Improvement
                4 points - Detailed and clear.
                3 points - General approach with some details.
                2 points - Vague approach.
                1 point - Approach not articulated.
            3. Real-World Application
                3 points - Concepts applied effectively to examples.
                2 points - Concepts somewhat applied.
                1 point - No application to real-world scenarios.
        """,
        "scored_phase": True,
        "minimum_score": 5,
    },
    "phase4": {
        "name": "Product Manager Interview - Summary",   
        "fields": {
            "question3_response": {
                "type": "markdown",
                "body": "Press submit to get overall feedback on the interview",
            }
        },
        "user_prompt": """Based on the conversation and the feedback you've provided, please now prioritize three key areas that I should work on to improve my interview skill.""", 
        "allow_skip": False,
        "ai_response": True,
        "button_label": "Get Overall Feedback"
    }
}




PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Mock Interview",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())