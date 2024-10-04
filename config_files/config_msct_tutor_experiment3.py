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



SYSTEM_PROMPT = """You are an expert clinical evaluator. You receive patient reports that include an initial diagnosis, you analyze all the symptoms carefully. You break down a diagnosis and look at it in several different ways to come to a conclusion. """


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
        #"user_prompt": """Here is a case. Please score it with a +1 for more likely, -1 for less likely, and 0 for neither more nor less likely: 
        #{my_disease}
        #""",
        "user_prompt": """Here is a case.
        {my_disease}

Please break down and repeat this case, with as much information as you have been given, but do not make up information. Use a format like the following, but again only include information when you know it to be accurate. Simply don't include information you don't have: 
## Clinical Scenario
  - Patient Information: [Age, Gender]
  - Chief Complaint: [Primary symptom or reason for visit]
  - History: [Relevant medical history, duration of symptoms, key findings]
## Initial Diagnosis: 
Initial Diagnosis: [Suspected condition]
##Additional Information
Additional Information: [New information from exam or tests]
        """,
        "ai_response": True,
        # "custom_response": DISEASE_GENERATOR[random_key]["case"],
        "allow_skip": False,
        "button_label": "Begin",
        "show_prompt": True
    },
    "step_2": {
        "name": "Initial Diagnosis",
        "fields": {
            "dummy1": {
                "type": "text_input",
                "label": "Dummy Field 1 (not used)",
                "value": "This field isn't used."
            }
        },
        "user_prompt": """
            Please Identify key terms and concepts in the clinical scenario and initial diagnosis, Analyze statistical associations based on medical literature and clinical guidelines, and Interpret the clinical scenario beyond simple keyword matching, considering the specific context.
            Make sure to Evaluate the case at multiple levels: individual symptoms, overall presentation, and potential underlying pathophysiology, and Consider how these layers of information interact and support or contradict each other.
            Your final output should be an initial hypothesis based on the presented information and your reasoning. 
        """,
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "semantic_entropy": {
        "name": "Semantic Entropy",
        "fields": {
            "dummy2": {
                "type": "text_input",
                "label": "Dummy Field 2 (not used)",
                "value": "This field isn't used."
            }
        },
        "user_prompt": """Please validate your initial hypothesis based on semantic entropy. Assess how the additional information affects diagnostic certainty. Semantic entropy is:
        Equation: H(D|S) = -∑P(D|S) * log₂P(D|S)
        Where:
        H(D|S) is the entropy of the diagnosis D given the symptoms S
        P(D|S) is the probability of the diagnosis given the symptoms

        Present your output as: 
        Semantic Entropy: [Semantic Entropy value]
""",
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "bayesian_update": {
        "name": "Bayesian Update",
        "fields": {
            "dummy3": {
                "type": "text_input",
                "label": "Dummy Field 3 (not used)",
                "value": "This field isn't used."
            }
        },
        "user_prompt": """Please Calculate how the new information changes the probability of the diagnosis, by performing a Bayesian update. Bayesian Update is expressed by the equation:
        P(D|S) = [P(S|D) * P(D)] / P(S)
        Where:
        P(D|S) is the posterior probability of the diagnosis given the symptoms
        P(S|D) is the likelihood of the symptoms given the diagnosis
        P(D) is the prior probability of the diagnosis
        P(S) is the probability of the symptoms

        Present your output as: 
        Bayesian Update: [Bayesian Update value]

""",
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "symptom_likelihood": {
        "name": "Symptom Likelihood",
        "fields": {
            "dummy4": {
                "type": "text_input",
                "label": "Dummy Field 4 (not used)",
                "value": "This field isn't used."
            }
        },
        "user_prompt": """Evaluate how likely the symptoms are given the hypothesized condition.
        This can be expressed as P(S|D) from the Bayesian equation above.

        Present your output as: 
        Symptom Likelihood: [Symptom Likelihood value]
""",
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "final_likert": {
        "name": "Final Likert Score",
        "fields": {
            "dummy5": {
                "type": "text_input",
                "label": "Dummy Field 5 (not used)",
                "value": "This field isn't used."
            }
        },
        "user_prompt": """Given the values you calculated above for Semantic Entropy, Bayesian Update, and Symptom Likelihood, in conjunction with your expert clinical knowledge and experience, arrive at a final assessment in the form of a likert score where +1 where the additional information makes the initial diagnosis more likely, -1 where it makes it less likely, and 0 where it makes it neither more nor less likely
        Make sure the output is in this format: 
        Likert Score: [likert value of +1, -1, or 0]
""",
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    }

}

PREFERRED_LLM = "gpt-4-turbo"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "MSC Tutor Experiment 3",
    "page_icon": "️🧑‍🏫",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

TEMPLATES = {"MSC Tutor Experiment 3":"config_msct_tutor_experiment3"}

from main import main
if __name__ == "__main__":
    config = {
        "APP_TITLE": APP_TITLE,
        "APP_INTRO": APP_INTRO,
        "APP_HOW_IT_WORKS": APP_HOW_IT_WORKS,
        "HTML_BUTTON": HTML_BUTTON,
        "PREFERRED_LLM": PREFERRED_LLM,
        "LLM_CONFIG_OVERRIDE": LLM_CONFIG_OVERRIDE,
        "PHASES": PHASES,
        "COMPLETION_MESSAGE": COMPLETION_MESSAGE,
        "COMPLETION_CELEBRATION": COMPLETION_CELEBRATION,
        "SCORING_DEBUG_MODE": SCORING_DEBUG_MODE,
        "DISPLAY_COST": DISPLAY_COST,
        "RAG_IMPLEMENTATION": RAG_IMPLEMENTATION,
        "SOURCE_DOCUMENT": SOURCE_DOCUMENT,
        "PAGE_CONFIG": PAGE_CONFIG,
        "SIDEBAR_HIDDEN": SIDEBAR_HIDDEN,
        "TEMPLATES": TEMPLATES
    }
    main(config)
