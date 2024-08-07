APP_TITLE = "Ebola Virus Ecology and Transmission (AI Assistants Template)"
APP_INTRO = """This is a simple app that assesses the user's understanding of a simple case study. It is for demonstrating the capabilities of a AI MicroApp. 
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

SYSTEM_PROMPT = """You are providing feedback on a shared case study about Ebola with the following content: 
# Ebola Virus Ecology and Transmission
Ebola is a zoonotic disease. Zoonotic diseases can be passed between animals and humans. 

## Animal-to-Animal Transmission
Evidence suggests that bats are the reservoir hosts for Ebola virus. Bats carrying the virus can transmit it to other animals, like apes, monkeys, and duikers (antelopes), as well as to humans. 

## Spillover Event
A "Spillover Event" occurs when an animal (bat, ape, monkey, duiker) or human becomes infected with Ebola virus through contact with the reservoir host. This contact could occur through hunting or preparing the animal's meat for eating. 

## Human-to-Human Transmission
Once the Ebola virus has infected the first human, transmission of the virus from one human to another can occur through contact with the blood and body fluids of sick people or with the bodies of those who have died of Ebola. 

## Survivor
Ebola survivors face new challenges after recovery. Some survivors report effects such as tiredness and muscle aches and can face stigma as they re-enter their communities. """

PHASES = {
    "about": {
        "name": "About the Case Study",
        "fields": {
            "about": {
                "type": "text_area",
                "height": 200,
                "label": """What is this case study about?""",
                "value": "The case study is about Ebola, and how it can be transmitted from animals to humans (a spillover event), humans to humans. It also includes details on how to support survivors returning to the community. ",
            }

        },
        "phase_instructions": "The user will summarize the shared case study. Please critically review their response for accuracy. You will give them credit for mentioning Ebola, and you will be very pleased if they mention it is about Ebola with any other relevant details.",
        "user_prompt": "{about}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
            1. About
                2 points - The user provides details that the case study is about Ebola and its transmission. 
                1 point - The user mentions the case study is about Ebola, but provides no further details. 
                0 points - The user does not accurately describe the shared case study. 
        """,
        "allow_revisions": False,
        "allow_skip": True,
        #"show_prompt": True,
        #"read_only_prompt": False
    },
    "spillover": {
        "name": "Define Spillover",
        "fields": {
            "spillover": {
                "type": "text_area",
                "height": 300,
                "label": """Describe a spillover event and how one might occur.""",
                "value": "A spillover event is when a virus jumps from one species to another, like from a bat to a monkey, or a monkey to a human. This occurs through direct contact with contaminated meat like eating an infected carcass or preparing raw meat.",
            }
        },
        "phase_instructions": "The user will describe a spillover event in the context of this shared document and how one might happen. Critically assess whether the user has accurately defined a spillover event and provided true examples for how one might happen. Provide feedback on their answer. If relevant, add further examples of how a spillover event might happen. ",
        "user_prompt": "{spillover}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
                1. Definition
                    1 point - The response accurately defines a spillover event
                    0 points - The response does not accurately define a spillover event.
                2. Examples
                    1 point - The response provides one or more plausible examples of how a spillover event might occur. 
                    0 points - The response does not provide any plausible examples of how a spillover event might occur. 
        """,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": True,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "reflection": {
        "name": "Reflect",
        "fields": {
            "reflection": {
                "type": "text_area",
                "height": 300,
                "label": "Imagine you are a public health worker in an area affected by Ebola. How might you ease the transition for survivors as they re-enter their communities?",
                "value":"Survivors could be supported by providing them leave as they manage their symptoms. Also by providing education to the community about the safety and struggles of survivors. Maybe a support group of survivors and supporters, too?",
            }
        },
        "phase_instructions": "The user will hypothesize about ways to support survivors as they re-enter the community. Critically evaluate their response to determine if they understand and have made a valid attempt to answer the question. If so, be supportive of their answer and their work on this exercise.",
        "user_prompt": "{reflection}",
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
