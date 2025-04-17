PUBLISHED = True
APP_URL = "https://video-reflection.streamlit.app"
APP_IMAGE = "video_reflection.webp"

APP_TITLE = "Sample Interview: Video Reflection Exercise"
APP_INTRO = """This app aims to demonstrate an AI-powered assessment that uses instructor guidance and AI support to encourage students to engage critically with an instructional video without first relying on AI.
1. First, a video is presented for the student to watch. Captions are burned in but not provided via full transcript. 
2. The student watches the video and answers an assessment. The questions, rubrics, and feedback guidance given to the AI are created by the educator.
3. Ideally, in this scenario the full transcript and any notes are shared with students after the assessment deadline has passed.

"""


SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """A user has watched a video and is answering questions about it. The questions might be factual or reflection questions. You will provide the user feedback based on instructions and grounded in evidence from the video. Here is the video transcript:
##VIDEO TRANSCRIPT
Welcome to the Digital Health in Medicine course.  Have you ever wondered how technology is transforming healthcare?  From telemedicine to wearable devices and the implementation of AI, digital health is revolutionizing how we deliver care and improve patient outcomes.  This free four week online course is your gateway to understanding the future of healthcare. 

Open to anyone with an interest in technology and healthcare. You'll dive into key concepts like electronic medical records, telemedicine, wearable tech, and the use of artificial intelligence in diagnostics.  Throughout this course, you'll explore evolving health policies, examine ethical considerations, and critically assess the role of AI in personalized medicine. 

Plus, you'll discuss the future trends shaping the healthcare industry,  whether you're a healthcare professional or just passionate about tech. This course will empower you to navigate the digital health landscape with confidence.  Sign up today and be part of the future of healthcare.  Join us on this exciting journey, because the future of healthcare starts with you. """


PHASES = {
    "phase1": {
        "name": "Watch the Video",
        "fields": {
            "question1_response": {
                "type": "markdown",
                "unsafe_allow_html": True,
                "body": """<p>Please watch the following video and continue.</p><iframe width="560" height="315" src="https://www.youtube.com/embed/N8x3D0ilRZs?si=YdRZts6ap_F9FMpU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""
            }
        },
        
        "ai_response": False,
        "custom_response": "Thanks for watching the video! Now, please answer some questions about it. Make sure to reference specific points from the video."
    },
    "phase2": {
        "name": "Think of Questions for this Course",
        "fields": {
            "questions": {
                "type": "text_area",
                "label": "After watching this video, what are two questions you'd like answered in this course? ",
                "height": 200,
                # "value": "First of all, how do we define health wearables? Are they any device that collect health data, or are they specifically devices used by hospitals?\nSecond, what role can AI chatbots play in healthcare? Could they be safe, even though we know they hallucinate?"
            }
        },
        "phase_instructions": "The user will provide two questions that they have based on watching this video. First identify the specific questions(s) that the user included in their response. For each question, identify if the user wrote their question using topics/evidence from the video. Lastly, encourage the user to seek answers to these questions as they go through the course.",
        "user_prompt": """{questions}. """,
        "ai_response": True,
        "allow_skip": False,
        "rubric": """
            1. Questions
                2 points - The user included at least two distinct questions.
                1 points - The user included only one distinct question in their response.
                0 point - The user did not include any questions in their response.
            2. Video Evidence
                2 points - The user included at least one specific topic/evidence from the video script per question.
                1 points - The user included one specific topic/evidence from the video script in total.
                0 point - The user did not include any specific details from the video. 
        """,
        "scored_phase": True,
        "minimum_score": 3,
    },
    "phase3": {
        "name": "Answer a Factual Question from the Video",
        "fields": {
            "length": {
                "type": "text_input",
                "label": "How long is this course?",
            }
        },
        "phase_instructions": "The user is simply telling you how long the course is, based on evidence from the video. Your response should be very brief and simply indicate if the user is correct or not, based on evidence from the video script.",
        "user_prompt": """{length}. """,
        "ai_response": True,
        "allow_skip": True,
        "rubric": """
            1. Questions
                1 points - The answer is correct
                0 point - The answer is incorrect.
        """,
        "scored_phase": True,
        "minimum_score": 1,
    },
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