APP_TITLE = "Modified Script Concordance Test (mSCT) Tutor"
APP_INTRO = """This is an AI tutor that presents interactive medical case studies with diagnosis and treatment scenarios. 

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
    
}

SYSTEM_PROMPT = """You create accurate script concordance tests and walk student through them. """

PHASES = {
    "about": {
        "name": "Choose a Disease",
        "fields": {
            "disease": {
                "type": "text_input",
                "label": """Enter a disease to practice your illness scripts.""",
                "value": "Strep Throat",
            }

        },
        "phase_instructions": """
        The user will give you a disease that they want to practice on. 

        Firstly, confirm that the user has given you a valid disease that you can provide a case study for. If not, please ask them to give you a valid disease and then stop and wait for their response. 
        
        If the user provides a valid disease, please generate a short case scenario statement that outlines a clinical presentation or problem that is related to an initial diagnosis, diagnostic testing, or treatment to the chosen disease. State the initial diagnosis based on the given case. This helps establish the starting point for their reasoning. 

        Then, generate a second statement related to an initial diagnosis, diagnostic testing, or treatment. Here you present a symptom, test result, or additional clinical information that could be relevant to a differential diagnosis or treatment choice. This information should allow for differentiation between the initial diagnosis and other potential options. 

        Finally, ask the user if 'the new information makes their decision [+1] More likely , [0] Neither more nor less likely, or [-1] Less likely ?
        It is important that this new information makes the likert score +1, 0, or -1. Do not always present +1 scenarios, but also 0, and -1. This second statement introduces elements of uncertainty in the initial diagnosis and is relevant to the specialty in question. 

        Use the following format: 
        Your next appointment is with a [Patient Description] that is being evaluated for [Symptom]. [Additional Patient History]. 

        If you were initially thinking of the following diagnosis/treatment: [Initial Diagnosis/Treatment], 

        and then you determine the following from the patient's history/exam/test results: [Additional Finding]. 

        Would the new information make my decision: 
        +1 More likely, 
        0 Neither more nor less likely, or 
        -1 Less likely"
        
        Here is a sample: 

        Case: Your next appointment is with a 60-year-old woman who is being evaluated for a chronic cough. She has a history of cough for 8 months, and during the examination, you auscultate a left apical systolic murmur.

        If you were initially thinking of the following diagnosis: Pulmonary edema (left-sided congestive heart failure)

        And then you determine the following from the patient's physical exam: Her heart rate is 70 beats/min, and thoracic auscultation reveals crackles bilaterally.

        Would the new information make my decision 
        +1 More likely, 
        0 Neither more nor less likely,
        -1 Less likely ?'
        """,
        "user_prompt": "{disease}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 1,
        "rubric": """
            1. About
                1 points - The user has provided a valid disease for which you can provide a case study
                0 points - The user has entered something other than a disease. 
        """,
        "allow_revisions": True,
        "allow_skip": False,
        #"show_prompt": True,
        #"read_only_prompt": False
    },
    "likert": {
        "name": "Score on the Likert Scale",
        "fields": {
            "likert": {
                "type": "selectbox",
                "options": ['+1 More likely', '0 Neither more nor less likely', '-1 Less likely'],
                "label": """Would the new information make your decision:""",   
                "index": 1
            }
        },
        "phase_instructions": "The user reacts to the second statement you provided with a likert scale rating indicating if they are more or less likely to stick with the original diagnosis. Simply acknowledge their rating (do not provide feedback at this point) and then ask them to provide written justification for their chosen Likert ranking.",
        "user_prompt": "{likert}",
        "ai_response": False,
        "custom_response": "Thank you for your rating! Now, please provide a written justification for your rating.",
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": True,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "rationale": {
        "name": "Explain your Rationale",
        "fields": {
            "rationale": {
                "type": "text_area",
                "height": 200,
                "label": "Please provide written justification for your chosen Likert ranking.",
            }
        },
        "phase_instructions": """
       The user will provide a written rationale for their ranking. 
       They should explain their thought process, how they used the key features or information to make their decision and provide a defense for their answer using background knowledge. 

       You will then generate a percentage estimated probability for the diagnosis, diagnostic testing, or treatment based on the information given. 
       For example: 'Estimated probability: 75%. Please note that this percentage is an educational guess and should not replace clinical judgment or professional diagnostic procedures.'
       Next, you generate a justification expected from typical expert responses. 
       For example: 'The presence of recurrent yeast infections in the patients history is more indicative of diabetes rather than hypothyroidism. Diabetes can lead to elevated blood sugar levels, creating a favorable environment for yeast overgrowth. In contrast, yeast infections are not typically associated with hypothyroidism. Therefore, the new information increases the likelihood of the initial diagnosis of diabetes.'
       Then, you compare your justification to that entered by the user, offering feedback comparing their choices to typical expert responses, and suggesting areas for improvement or affirmation. 
        """,
        "user_prompt": "{rationale}",
        "ai_response": True,
        "scored_phase": False,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": True,
        "show_prompt": False,
        "read_only_prompt": False
    }

}

PREFERRED_LLM = "gpt-4-turbo"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False