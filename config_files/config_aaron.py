APP_TITLE = "Aaron's Test"
APP_INTRO = """In this interactive exercise, you will participate in a structured debate with an AI, which challenges your reasoning and enhances your argumentative skills across various topics. After choosing a topic and a position to take, you'll engage in three rounds of debate, responding to the AI's prompts and refining your arguments. The exercise concludes with a summary from the AI, highlighting key points and providing feedback on your strengths and areas for improvement. Get ready to critically engage and articulate your thoughts in this casual virtual debate setting. 
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
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    "url": "https://curricume-uploads.s3.amazonaws.com/cdc_ebola_poster.pdf",
    "button_text":"Read PDF"
}

SYSTEM_PROMPT = """You provide feedback on a natural language short answer quiz about a man named Aaron. You never give the answer and you start by saying whether the user is correct or incorrect with their answer. """

PHASES = {
    "history": {
        "name": "Aaron's History",
        "fields": {
            "street": {
                "type": "text_area",
                "height": 200,
                "label": """What street did Aaron grow up?""",
                "value": "",
            }

        },
        "phase_instructions": "The user will name the street that Aaron grew up. THe answer is Park Ave.",
        "user_prompt": "{street}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 1,
        "rubric": """
            1. About
                1 point - The user mentions that Aaron grew up on Park ave
                0 points - The user does not accurately say that Aaron grew up on Park Ave
        """,
        "allow_revisions": False,
        "allow_skip": True,
        #"show_prompt": True,
        #"read_only_prompt": False
    },
    "work": {
        "name": "Work",
        "fields": {
            "work": {
                "type": "text_area",
                "height": 300,
                "label": """What does Aaron do for work""",
                "value": "",
            }
        },
        "phase_instructions": "The user explains what aaron does for work. Aaron is a handyman or general contractor.",
        "user_prompt": "{work}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 1,
        "rubric": """
                1. Work
                    1 point - THe user responds that Aaron does something in the trades, like handyman or genearl contractor
                    0 points - The response does not accurately reflect Aaron's work in the trades.
                
        """,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": True,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "architecture": {
        "name": "architecture",
        "fields": {
            "architecture": {
                "type": "text_area",
                "height": 300,
                "label": "What are the important aesthetic elements of quality architecture?",
                "value":"",
            }
        },
        "phase_instructions": "The user reflects on the important aesthetic elements of quality architecture. Provide constructive feedback on their reflection. Tell them what the general consensus mostly agrees with and what they disagree with.",
        "user_prompt": "{architecture}",
        "ai_response": True,
        "scored_phase": False,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": True,
        "show_prompt": False,
        "read_only_prompt": False
    }

}
    
PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
