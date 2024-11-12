APP_URL = "https://clinical-chatbot.streamlit.app"
APP_IMAGE = "clinical_chatbot.webp"
PUBLISHED = True

APP_TITLE = "Clinical Chatbot"
APP_INTRO = """
In this interactive exercise, you will interact with a clinical chatbot that will help you understand your patient's condition. You must determine their primary complaint and provide a differential diagnosis.
"""

APP_HOW_IT_WORKS = """
This app provides a structured way to interact with an AI-powered clinical chatbot.

The chatbot has been provided with a patient history and a list of symptoms. Your job is to determine the primary complaint and provide a differential diagnosis.

The user will be able to have a free-form conversation with the chatbot to clarify their condition. Then they will input their primary complaint and a differential diagnosis.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You are an assistant for a clinical simulation exercise for a student user who is playing the role of a doctor. You will answer the user's questions and sometime assess their accuracy.
"""

PHASES = {
    "interview": {
        "name": "Patient Interview: Donna",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<p>Donna is a new patient in your office. She is a 65-year old woman who has been experiencing shortness of breath for the past 2 weeks. She is a smoker and has a history of hypertension. You only have <strong>15 minutes</strong> to interview Donna and determine her primary complaint and differential diagnosis. For this simulation, that means you'll be able to ask her up to 10 questions.</p>""",
                "unsafe_allow_html": True,
            },
            "patient_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "app_images/donna.webp",
                "caption": "Your new patient Donna is a 65-year old woman with a history of hypertension and currently experiencing shortness of breath.",
            },
            "chat": {
                "type": "chat_input",
                "max_messages": 10,
                "placeholder": "Ask Donna something...",
                "initial_assistant_message": "Hi Doctor, can you help me with my recent breathing issues?"
            }
        },
        "phase_instructions": """For this chat, you play the role of a 65-year old woman named Donna with a history of hypertension and currently experiencing shortness of breath. The user is playing the role of a doctor. You will be asked questions by the doctor and respond with a short answer.
        Here is more information about Donna:
        Here is the information for your role:
Patient Name: Donna
Age: 65
Gender: Female
Chief Complaint: Shortness of breath, experienced for the past 2 weeks.

# Patient History:
1. Medical History:

    a. Hypertension: Diagnosed approximately 15 years ago and has been managed with antihypertensive medication (specify if known).
    b. Smoking History: Current smoker, with a smoking history of approximately X pack-years (estimated at 1 pack per day for 40+ years). The exact duration and pack count would need to be confirmed.
    c. No Known Allergies.
2. Family History:

    a. Mother: Died from complications of cardiovascular disease at age 70.
    b. Father: History of lung disease (chronic bronchitis) and died of emphysema at age 75.
    c. Siblings: Brother with type 2 diabetes, sister with hypertension.
3. Social History:

    a. Lifestyle: Sedentary; occasional walks but not regular exercise.
    b. Diet: No specific dietary restrictions; consumes processed foods occasionally, moderate salt intake.
    c. Alcohol Consumption: Social drinker, approximately 2 drinks per week.
    d. Occupation: Retired, previously worked as a schoolteacher.
4. Medications:

    a. Amlodipine: For blood pressure management, taken daily.
    b. Aspirin: Low-dose, taken daily for cardiovascular protection.
    c. Over-the-counter cough suppressant: Recently began taking for relief from mild coughing spells accompanying her shortness of breath.

# Primary Symptoms:

1. Shortness of Breath (Dyspnea):

    a. Duration: 2 weeks.
    b. Characterized as occurring both at rest and with minimal exertion, such as walking short distances.
    c. No history of similar symptoms in the past.
    d. No significant improvement with rest.
    e. Difficulty breathing more pronounced when lying flat (orthopnea).
2. Chronic Cough:

    a. Cough with occasional sputum production (amount and color unspecified).
    b. Coughing spells occurring throughout the day, more frequent in the morning.
# Secondary Symptoms:
1. Fatigue:
    a. Generalized tiredness and reduced energy levels over the past 2 weeks.
    b. More noticeable than her usual baseline fatigue.
2. Chest Discomfort:
    a. Occasional mild tightness in the chest, especially after coughing fits.
    b. No reported radiation of pain to the arms, jaw, or back.
3. Mild Edema:
    a. Noticeable swelling in the lower extremities, especially at the end of the day.
    b. Slight improvement after elevating legs.
4. Intermittent Dizziness:
    a. Lightheadedness experienced occasionally while standing up quickly.  
    b. Possibly related to her blood pressure medication.
        """,
        "user_prompt": """From the chat, provide feedback on the following: 
        1. Whether the doctor is asking appropriate questions.
        2. Whether the doctor has an appropriate bedside manner and makes the patient feel comfortable. 
        3. Whether the doctor is staying on topic.

        Begin your response with "Here is some feedback on your chat with Donna:"
        """,
        "ai_response": True,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "primary_complaint": {
        "name": "Primary Complaint",
        "fields": {
            "primary_complaint": {
                "type": "text_input",
                "label": "What is the user's primary complaint?",
            },
            "diagnosis": {
                "type": "text_area",
                "height": 200,
                "label": "Establish a differential diagnosis for Donna.",
            }
        },
        "phase_instructions": """The user will provide you with the patient's primary complaint and her differential diagnosis. You will provide feedback on the accuracy of their claim(s) based on the evidence they gathere in the conversation.
        
        Here are some more details:     
    # Differential Considerations:
1. Chronic Obstructive Pulmonary Disease (COPD):
    a. Likely given her smoking history, cough, and recent onset of dyspnea.
    b. Recommend spirometry and imaging (chest X-ray or CT) for confirmation.
2. Congestive Heart Failure (CHF):
    a. Possibility due to dyspnea, edema, and history of hypertension.
    b. Further investigation with echocardiography and BNP levels would be useful.
3. Pulmonary Hypertension or Pulmonary Embolism:
    a. While less common, consider ruling out due to sudden onset of symptoms and history of smoking.
4. Lung Cancer:
    a. Given her age and smoking history, screening might be advisable.

# Plan for Further Evaluation:
1. Diagnostic Imaging:
    a. Chest X-ray or CT scan to evaluate lung structure.
2. Laboratory Tests:
    a. Basic metabolic panel, BNP, D-dimer (if PE suspected).
3. Pulmonary Function Tests (PFTs):
    a. Spirometry to assess for COPD or restrictive lung disease.
4. Electrocardiogram (ECG):
    a. To assess any cardiac involvement, such as ischemia or arrhythmia.""",
        "user_prompt": "Donna's primary complaint is: {primary_complaint}. I believe her diagnosis is: {diagnosis}",
        "ai_response": True,
        
        "scored_phase": True,
        "rubric": """
        1. Primary Complaint:
        2 points - The user has provided a primary complaint that is consistent with Donna's presentation and that they've extracted from the chat with Donna.
        0 points - The user has provided a primary complaint that is not consistent with Donna's presentation or they did not extract it from the chat with Donna..
        2. Differential Diagnosis:
        2 points - The user has provided a differential diagnosis that is consistent with Donna's presentation and that they've extracted from the chat with Donna.
        0 points - The user has provided a differential diagnosis that is not consistent with Donna's presentation or they did not extract it from the chat with Donna.
        """,
        "minimum_score": 2,
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
    "page_title": "Clinical Chatbot",
    "page_icon": "⚕️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())