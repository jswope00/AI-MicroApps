APP_TITLE = "SOAP Notes Feedback"
APP_INTRO = """This app provides feedback on written SOAP (subjective, objective, assessment, and plan) notes. It provides feedback in stages for more precision over the feedback provided. . 
"""

APP_HOW_IT_WORKS = """
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You grade medical students' soap notes based on a rubric. 
When a user's answer is accurate, you don't need to provide verbose feedback. 
When a user's answer is inaccurate, you can provide very brief 1-2 sentence supportive hint about how they might get the right answer next time. 
Your primary focus is scoring based on a rubric. You should prioritize getting the score right by first using the information given to you in the rubric and other prompts, and secondarily by going to your general knowledge. """

PHASES = {
    "phase1": {
        "name": "Patient History",
        "fields": {
            "patient_history": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste the PATIENT HISTORY section of your note""",
                "value": """Chief complaint: I am having darker than usual urine 

HPI: MJ is a 35 y/o female who presents today complaining of a 1 week history of blood in her urine. Patient reports there is pain associated with it and rates it 6 out of 10. Pain radiates to groin, nothing makes it better or worse. Patient reports taking Ibuprofen 800 mg TID for the past week. Patient reports she feels abdominal fullness even with a little bit of food and pain in the right side of her back. Patient has not had prior episode of this. No skin discoloration. Patient states happens everyday not at the same time and the color is dark red to brown. 

PMH: HTN x 7 years No surgeries 

Medications: Lisinopril 20 mg 1x a day for past 7 years and Amlodipine 10 mg x7 years 1 x per day 

Vaccinations: Up to date 

Allergies: None 

Family hx: Father is fine, Mother has hx of HTN and surgery for bleed in brain, brother is fine 

Social hx: Social drinker 1-2 cups of wine per outing and 10 years of smoking 1 pack per day No illicit drug use 

Occupation: Taxi driver for the past 10 years Diet chicken fish vegetables that are grilled or baked. No exercise 

Sexual hx: Yes active, 1 partner, No protection yes STD testing 5 years ago and 
was negative. No children and last cycle was 2 weeks ago and is regular. """
            }
        },
        "phase_instructions": """Confirm that the user has adequately capture the patient history, especially the main symptom. Here are the relevant patient history details: 
        Main symptom/Cardinal Symptoms - Dark urine
            The urine is dark red to brown like blood throughout the stream with no clots and no odor.
            It occurred every day of the week but not with every urination.
            No previous history of this symptom.
            There is no urinary frequency, nocturia, polyuria, dysuria, changes in the stream, or dribbling
        Associative Symptom: Flank Pain
            Pain in right flank x 1 month – sudden, intermittent, dull radiating to the right groin area, 3/10 initially and 6/10 for the past week, nothing makes the pain worst and it is not relieved by ibuprofen.
        Associative Symptom: Abdominal/Early fullness
            Early fullness/ (Early satiety) x 3 months – eating very little and becoming full. Nothing seems to make it worse, better, or precipitates it.
        Pertinent Negatives: *no associated appetite changes, fever, nausea, vomiting, diarrhea, constipation, blood in stool, no weight loss. No history of renal stones/UTIs. """,
        "user_prompt": "{patient_history}",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
            1. Organization
                5 points - The history is consistently organized and contains appropriately labeled sections and sub-sections (CC, HPI, and relevant contributing history). 
                3.75 points - The history is somewhat organized and contains appropriate sections (CC, HPI, and relevant contributing history). 
                2.5 points - The history is somewhat organized but is missing sections and/or section labels. 
                1.25 points - The history is poorly organized. 
                0 points - The history is not organized. 
            1. History of Present Illness
                15 points - History contains all the relevant attributes of the patient's presenting complaint (cardinal features, pertinent negative symptoms) AND is presented in chronological order. 
                11.25 points - History contains most of the relevant attributes of the patient's presenting complaint (cardinal features, pertinent negative symptoms) AND is presented in chronological order. 
                7.5 points - History contains some of the relevant attributes of the patient's presenting complaint (cardinal features, pertinent negative symptoms) OR has some inconsistencies in the timeline. 
                3.75 points - History contains some of the relevant attributes of the patient's presenting complaint (cardinal features, pertinent negative symptoms) AND has some inconsistencies in the timeline. 
                0 points - History does not contain relevant attributes of the patient's presenting complaint (cardinal features, pertinent negative symptoms) AND has many inconsistencies in the timeline. 
            4. Additional History
                10 points - Additional history contains all information to support diagnostic reasoning. 
                7.5 points - Additional history contains most but not all information to support diagnostic reasoning. 
                5 points - Additional history contains some information to support diagnostic reasoning. 
                2.5 points - Additional history contains some information to support diagnostic reasoning, AND there are factual inaccuracies. 
                0 points - Additional history is insufficient to support diagnostic reasoning. 
        """,
        "minimum_score": 5
    },
    "phase2": {
        "name": "Physical Exam",
        "fields": {
            "physical_exam": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste the PHYSICAL EXAM section of your note""",
                "value": """PE: 
VS: T: 98.2, BP160/110 HR 90 recheck is 64, and Resp are 14 per min 
G/A: Well appearing female, awake, alert, and oriented x3 in no apparent painful distress. 

Abd: No scarring, no contours, no deformities, tenderness on the right flank + kidney ballotment on the right, no bruit in the right or left renal artery. No 
abdominal bruit, no tenderness in the 9 front quadrants, normal bowel sounds 
present in all quadrants on auscultation. 

Cardio: S1,S2 present, no S3 no S4, no gallops, no murmurs. 

US: + multiple cysts on bilateral kidneys + calculus in r. kidney 
Urinalysis: + RBC, +3 heme, Cloudy urine, +WBC, no casts. """
            }
        },
        "phase_instructions": """Confirm that the user has adequately capture the physical examination notes. Provide critical feedback based on this answer key: 
       General Appearance: The user should include some comment on general appearance. 
       Vital Signs: T:36.9 C(98.2 F) HR:90  RR: 14 BP: 160/110
       Abodmen: The user should include some comment on inspection of abdomen.
       Abodmen Palpatation: The user should include some comment on light and deep palpation of abdomen.
       Liver: The user should include some comment on Liver Span and Liver Palpation (Hepatomegaly)
       Splenic percussion: The user should include some comment on Splenic percussion and palpation (Splenomegaly)
       Kidneys: The user should include some comment on Right & Left Kidneys (e.g. Kidneys are not palpable OR not ballotable bilaterally. )
       Abodmen: The user should include some comment on generalized percussion of Abdomen. (E.g. Abdomen is tympanic throughout)
       CVA Tenderness: The user should include some comment on CVA tenderness of Right and Left Kidney. (E.g. No costovertebral (CVA) tenderness OR Right CVA tenderness. )""",
        "user_prompt": "{physical_exam}",
        "allow_skip": True,
        "scored_phase": True,
 "rubric": """
            1. Organization
                5 points - Physical examination is organized and labeled into clear sections and presented in a systematic manner. It contains the general assessment & vital signs. 
                3.75 points - Physical examination is organized and labeled into sections. It contains the general assessment & vital signs. 
                2.5 points - Physical examination is somewhat organized and labeled into sections. It contains the general assessment & vital signs. 
                1.25 points - Physical examination has some accurte details and some innacurate. 
                0 points - Physical examination is not organized and does not contain general assessment and vital signs. 
            2. Physical Examination
                10 points - The physical examination section contains complete, accurate, and logical documentation of the relevant system for the patient's presenting complaint. 
                7.5 points - The physical examination section contains mostly complete, accurate, and logical documentation of the relevant system for the patient's presenting complaint. 
                5 points - The physical examination section contains partially complete, accurate, and logical documentation of the relevant system for the patient's presenting complaint. OR it contains some factual errors. 
                2.5 points - The physical examination section contains partially complete, accurate, and logical documentation of the relevant system for the patient's presenting complaint. AND it contains some factual errors. 
                0 points - Physical examination was not relevant to the patient's presenting complaint. 
            3. Additional Examinations
                10 points - Documentation of complete and accurate additional physical examination relevant to differential diagnosis with no factual errors. 
                7.5 points - Documentation of most additional physical examination relevant to differential diagnosis with no factual errors. 
                5 points - Documentation of some additional physical examination relevant to differential diagnosis OR contains a few factual errors. 
                2.5 points - Documentation of few additional physical examination relevant to differential diagnosis AND contains a few factual errors. 
                0 points - No documentation of additional physical examinations relevant to support the differential diagnosis. 
        """,
        "minimum_score": 2
    },
    "phase3": {
        "name": "Differential Diagnosis",
        "fields": {
            "ddx": {
                "type": "text_area",
                "height": 400,
                "label": "Please paste differential diagnosis notes here",
                "value": """
DDX 1: Polycystic Kidney disease - HTN -Family hx is postive for berry aneurysm in mother and HTN -R. flank pain - RBC from investigation positive - Heme 3+ positive - US of abdomen showed multiple cysts on both kidneys 

DDX 2: Nephrolithiasis - US of abdomen shows L sided calculus - Flank pain Cysts on both kidneys visualized on US - Dark urine 

DDX 3: Berger's disease - Blood in urine - Heme +3 - Smoker x 10 years - Age range is 30-40 - HTN 

""",
            }
        },
        "phase_instructions": "Confirm that the user has adequately provided a list of differential diagnosis options, ranked in order of likelihood, and supported by details from the patient examination and/or history. ",
        "user_prompt": "{ddx}",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
            1. List
                10 points - The assessment contains three discrete diseases, with each being relevant to the patient’s presentation
                7.5 points - The assessment contains at least two discrete diseases, with each being relevant to the patient’s presentation. 
                5 points - The assessment contains at least two discrete diseases, but one is irellevant to the patient's presentation.
                2.5 points - The assessment contains only one discrete disease option.
                0 points - The assessment does not contain any discrete or relevant diagnosis. 
            2. Ranking
                15 points - All differential diagnoses are listed in order of most likely diagnosis, and each is relevant to the patient’s presentation. 
                11.25 points - All differential diagnoses are listed in order of most likely diagnosis, but one is not relevant to patient's presentation. 
                7.5 points - Leading diagnosis is not the most likely diagnosis in the differential but contains at least two discrete diseases and each is relevant to the patient presentation. 
                3.75 points - Leading diagnosis is not the most likely diagnosis in the differential but contains at least one discrete diseases which is relevant to the patient presentation. 
                0 points - Differential diagnosis not listed in order of most likely diagnosis and does not contain any discrete or relevant diagnosis. 
            3. Support
                10 points - Differential diagnoses are consistently supported by at least three (3) relevant subjective or objective history. 
                7.5 points - Differential diagnoses are consistently supported by at 2-3 relevant subjective or objective history, and are factually accurate. 
                5 points - Differential diagnoses are somewhat supported by relevant subjective or objective history but contain some factual errors. 
                2.5 points - Differential diagnoses are loosely supported by relevant subjective or objective history and contain factual errors. 
                0 points - Differential diagnoses are not supported by relevant subjective or objective history. 
        """,
        "minimum_score": 2
    },
    "phase4": {
        "name": "Patient Plan",
        "fields": {
            "patient_plan": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste the PATIENT PLAN section of your note""",
                "value": """Urinalysis, US of abdomen, and cbc with diff continue current medications - consult to nephrology and follow up in a week."""
            }
        },
        "phase_instructions": """Confirm that the user has adequately provided a plan with investigations that are relevant to the differential diagnosis.""",
        "user_prompt": "{physical_exam}",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
            1. Relevant Patient Plan
                10 points - The plan consists of investigations and/or physical examinations and are consistently relevant to the differential diagnoses corresponding to the patient’s encounter. 
                7.5 points - The plan consists of investigations and/or physical examinations and are mostly relevant to the differential diagnoses corresponding to the patient’s encounter. 
                5 points - The plan has some investigations and/or physical examinations relevant to the differential diagnoses corresponding to the patient’s encounter. 
                2.5 points - The plan contains some relevant and some irrelevant investigations and/or physical examinations corresponding to the patients differential diagnoses. 
                0 points - The plan is not relevant to the differential diagnoses corresponding to the patient’s encounter. 
        """,
        "minimum_score": 2
    }

}

PREFERRED_LLM = "gpt-4-turbo"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
