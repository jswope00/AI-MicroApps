import random

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

DISEASE_GENERATOR = {
    "1_1": {
        "initial_diagnosis": "Chronic Asthma",
        "case": """Your next appointment is with a 79-year-old man who is being evaluated for cough. He has a
history of cough for 6 months and you auscultate a grade 4/6 left apical systolic murmur during
the exam.

If you were initially thinking of the following diagnosis: Chronic asthma,

And then you determine the following from the patient&#39;s history: He has normal lung
function tests (FEV1/FVC and FVC).""",
        "answer": "The diagnosis becomes less likely (-1).",
        "justification": "Normal lung function is possible in chronic asthma, but unlikely in an elderly chronic asthmatic."
    },
    "1_2": {
        "initial_diagnosis": "COPD",
        "case": """Your next appointment is with a 79-year-old man who is being evaluated for cough. He has a
history of cough for 6 months, and you auscultate a grade 4/6 left apical systolic murmur during
the exam.

If you were initially thinking of the following diagnosis: COPD,

And then you determine the following from the patient&#39;s history: The cough occurs
during forced exhalation and is accompanied by wheezing due to dynamic airway
collapse.""",
        "answer": "The diagnosis becomes more likely (+1).",
        "justification": "COPD is characterized by chronic bronchitis and emphysema, which can present with a cough, especially during forced exhalation, and wheezing due to airway collapse. Note that dynamic airway collapse is not a measure used for diagnosis."
    },
    "1_3": {
        "initial_diagnosis": "Pulmonary Edema",
        "case": """Your next appointment is with a 79-year-old man who is being evaluated for cough. He has a
history of cough for 6 months and you auscultate a grade 4/6 left apical systolic murmur during
the exam.

If you were initially thinking of the following diagnosis- Pulmonary edema (left-sided
congestive heart failure CHF),

And then you determine the following from the patient&#39;s history: The cough has become
more frequent in the past 48 hours.""",
        "answer": "The diagnosis becomes neither more nor less likely (0).",
        "justification": "Many things can cause an acute worsening of a chronic symptom, e.g., viral infection. While an increase in the frequency of the cough could be indicative of worsening heart failure, it is not specific enough to significantly alter the likelihood of pulmonary edema without additional supporting symptoms or findings such as dyspnea, orthopnea, or paroxysmal nocturnal dyspnea."
    },
    "2_1": {
        "initial_diagnosis": "Pulmonary Edema",
        "case": """Your next appointment is with a 60-year-old woman who is being evaluated for cough. She
has had a cough for 8 months, and you auscultate a grade 4/6 left apical systolic murmur during
the exam.

If you were initially thinking of the following diagnosis: Pulmonary edema (left sided
congestive heart failure),

And then you determine the following from the patient&#39;s physical exam: Her heart rate is
70 beats/min, and thoracic auscultation reveals crackles bilaterally.""",
        "answer": "The diagnosis becomes more likely (+1).",
        "justification": "Diagnosis is reasonable given the age and duration of symptoms. The presence of crackles supports the diagnosis of pulmonary edema secondary to left-sided congestive heart failure."
    },
    "2_2": {
        "initial_diagnosis": "COPD",
        "case": """Your next appointment is with a 60-year-old woman who is being evaluated for cough. She
has a history of cough for 8 months and you auscultate a grade 4/6 left apical systolic murmur
during the exam.

If you were initially thinking of the following diagnosis- COPD,

And then you determine the following from the patient&#39;s physical exam: The patient is a
smoker, the cough occurs in the morning, and lung auscultation reveals crackles
bilaterally.""",
        "answer": "The diagnosis becomes neither more nor less likely (0).",
        "justification": "Smoking history and morning cough are consistent with COPD, but the presence of bilateral crackles is more suggestive of chronic heart failure."
    },
    "2_3": {
        "initial_diagnosis": "Pulmonary Edema",
        "case": """Your next appointment is with a 60-year-old woman who is being evaluated for cough. She
has a history of cough for 8 months and you auscultate a grade 4/6 left apical systolic murmur
during the exam.

If you were initially thinking of the following diagnosis: Pulmonary edema (left-sided
congestive heart failure),

And then you determine the following from the patient&#39;s physical exam: Her heart rate is
120 beats/min, and her respiratory rate is 10 breaths/min.""",
        "answer": "The diagnosis becomes neither more nor less likely (0).",
        "justification": "As a note, if HR is 120, it’s extremely unlikely the respiratory rate is 10, and there is likely an error in the exam. Both findings are contradictory to each other to support the initial diagnosis, and further information or redoing the exam is needed."
    },
    "3_1": {
        "initial_diagnosis": "Chronic bronchitis",
        "case": """You are presented with a 52-year-old man who is being evaluated for a cough that he has had
for 7 months. He describes the cough as harsh and occurs with activity. On examination, he is
bright and alert. His mucous membranes are pink and moist with a normal capillary refill time.
His heart rate is 70 beats/min and femoral pulses are strong bilaterally. His respiratory rate is 14
breaths/min. A grade 4/6 left apical systolic murmur was auscultated.

If you were initially thinking of the following diagnosis: Chronic bronchitis,

And then you determine the following from the patient&#39;s physical exam: When
auscultating the lung fields, crackles are heard bilaterally.""",
        "answer": "The diagnosis becomes less likely (-1).",
        "justification": "The presence of bilateral crackles suggests lung disease, but there is a disconnect with his cough, and there is a lack of detail e.g. productive, and shortness of breath."
    },
    "3_2": {
        "initial_diagnosis": "Pulmonary Edema",
        "case": """You are presented with a 52-year-old man who is being evaluated for a cough that he has had
for 7 months. He describes the cough as harsh and occurs with activity. On examination, he is
bright and alert. His mucous membranes are pink and moist with a normal capillary refill time.
His heart rate is 70 beats/min and femoral pulses are strong bilaterally. His respiratory rate is 14
breaths/min. A grade 4/6 left apical systolic murmur was auscultated.

If you were initially thinking of the following diagnosis: Pulmonary edema (left-sided
congestive heart failure),

And then you determine the following from the patient&#39;s physical exam: When
auscultating the lung fields, crackles are heard bilaterally.""",
        "answer": "The diagnosis becomes neither more nor less likely (0).",
        "justification": "Bilateral crackles are consistent with pulmonary edema but can also be present in other conditions such as interstitial lung disease or pneumonia. Their presence alone does not confirm or rule out the diagnosis of pulmonary edema."
    },
    "4_1": {
        "initial_diagnosis": "Innocent Murmur",
        "case": """Your next appointment is with a 4-month-old girl for her well-child exam. She has a history
of an occasional cough for the past few days. Her appetite and activity level are normal

according to her parents. On physical examination, she is bright and alert with pink mucus
membranes, and is normal size for her age. You auscultate a murmur during the exam.

If you were initially thinking of the following diagnosis: Innocent murmur,

And then you determine the following from the patient&#39;s physical exam: The murmur is a
grade 2/6 that is systolic and heard best at the left base.""",
        "answer": "The diagnosis becomes less likely (-1).",
        "justification": "2/6 is pretty loud for something innocent. In the absence of delayed motor milestones, or abnormal exam finding, I do not believe the cough is related to the incidental finding of a 2/6 murmur."
    },
    "4_2": {
        "initial_diagnosis": "Patent ductus arteriosus",
        "case": """Your next appointment is with a 4-month-old girl for her well-child exam. She has a history
of an occasional cough for the past few days. Her appetite and activity level are normal
according to her parents. On physical examination, she is bright and alert with pink mucus
membranes, and is normal size for her age. You auscultate a murmur during the exam.

If you were initially thinking of the following diagnosis: Patent ductus arteriosus,

And then you determine the following from the patient&#39;s physical exam: The murmur is a
palpable grade 5/6. It is loudest at the left upper sternal border and is continuous,
occurring throughout systole and diastole.""",
        "answer": "The diagnosis becomes more likely (+1).",
        "justification": "The murmur is loud (grade 5/6), continuous, and location is consistent with patent ductus arteriosus (PDA)."
    }

}

# Select a random key from the DISEASE_GENERATOR dictionary
random_key = random.choice(list(DISEASE_GENERATOR.keys()))



SYSTEM_PROMPT = """You are an expert clinical evaluator. You receive patient reports that include an initial diagnosis, you analyze all the symptoms carefully. You also receive a complicating factor, and based on the complicating factor you assess whether the original diagnosis is more likely, less likely, or neither more nor less likely."""

PHASES = {
    "about": {
        "name": "Choose a Disease",
        "fields": {
            "disease": {
                "type": "markdown",
                "body": """To begin, the system will select a case for you to practice on.""",
                "unsafe_allow_html": True
            },
            "my_disease": {
                "type": "text_area",
                "label": "chosen disease",
                "height": 200,
                "value": DISEASE_GENERATOR["2_3"]["case"]
            }

        },
        "user_prompt": """Here is a case. Please score it with a +1 for more likely, -1 for less likely, and 0 for neither more nor less likely: 
        {my_disease}

        Make sure the output is in this format: 
        Likert Score: [likert value of +1, -1, or 0]
        """,
        "ai_response": True,
        # "custom_response": DISEASE_GENERATOR[random_key]["case"],
        "allow_skip": False,
        "button_label": "Begin",
        "show_prompt": True
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
        "phase_instructions": f"""
       The user will provide a written rationale for their ranking. 
       They should explain their thought process, how they used the key features or information to make their decision and provide a defense for their answer using background knowledge. 

       You will then generate a percentage estimated probability for the diagnosis, diagnostic testing, or treatment based on the information given. 
       For example: '**Probability** \n\nEstimated probability: 75%. Please note that this percentage is an educational guess and should not replace clinical judgment or professional diagnostic procedures.'
       Next, you generate a justification expected from typical expert responses. 
       For example: '**Expert Justification**\n\nThe presence of recurrent yeast infections in the patients history is more indicative of diabetes rather than hypothyroidism. Diabetes can lead to elevated blood sugar levels, creating a favorable environment for yeast overgrowth. In contrast, yeast infections are not typically associated with hypothyroidism. Therefore, the new information increases the likelihood of the initial diagnosis of diabetes.'
       Then, you determine if the user's answer matched the correct answer of {DISEASE_GENERATOR[random_key]["answer"]}. If it does not match, provide an explanation for what might have led the student to the wrong answer and a recommendation on how to avoid that mistake in the future. 
       For example: '**Diagnosis**\n\nYour answer of [user answer e.g. -1, 0, +1] did not match my expected answer. Remember that strep throat is a bacterial infection, so viral indicators may not increase the likelihood of strep throat'
       Then, you compare the correct justification to that entered by the user, offering feedback comparing their choices to the correct justification, and suggesting areas for improvement or affirmation. 
       For example: '**Feedback**\n\nIt’s commendable that you identified the complexity introduced by the additional cardiac symptoms and did not solely fixate on the respiratory symptoms, which could lead to a narrow differential diagnosis. Going forward, continue to consider the entire clinical picture and how various symptoms can interconnect. This holistic approach will enhance your diagnostic accuracy.'
        Correct Justification: {DISEASE_GENERATOR[random_key]["justification"]}
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