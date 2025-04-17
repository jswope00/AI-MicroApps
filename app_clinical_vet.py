APP_URL = "https://clinical-chatbot.streamlit.app"
APP_IMAGE = "clinical_chatbot.webp"
PUBLISHED = True

APP_TITLE = "Case Study: Champ the Sunbathing Dog"
APP_INTRO = """
In this simulation, you will play the role of a veterinarian having a conversation with the owner of a dog "Champ" who has not been as active as normal.
"""

APP_HOW_IT_WORKS = """
This app provides a structured way for you to interact with the dog owner to better understand the condition of "Champ".

You will plan your consultation, speak to the owner, perform a physical exam, and provide a diagnosis.
"""

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You are an assistant for a clinical simulation exercise for a student user who is playing the role of a veterinarian. You will answer the user's questions and sometimes assess their accuracy.
"""

PHASES = {
    "plan_consultation": {
        "name": "Plan your Consultation",
        "fields": {
            "about": {
                "type": "markdown",
                "body": """<h2>Learning Objectives</h2>
                           <p>By the end of this lesson, you will be able to:</p><ol>
                           <li>Identify and document details from the history that may not be selected as problems but could be relevant to the case workup.</li>
                           <li>Formulate a problem list from signalment, presenting complaint, history, and clinical exam.</li>
                           <li>Recognize the clinical signs of dehydration versus hypovolemia</li></ol>""",
                "unsafe_allow_html": True,
            },
            "case_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "https://d2jqdwayv0rru6.cloudfront.net/microapp-images/dog1.webp",
                "caption": "Champ is a young Pothound who has not been as active lately.",
            },
            "phone_call": {
                "type": "markdown",
                "body": """<h2>Phone Call</h2><p>You are a recently graduated veterinarian practicing in Grenada. On a hot, dry March morning, Mrs. Charles called the clinic you are currently working at about Champ. Champ is a young Pothound that Mrs. Charles has owned since he was a puppy. She says that Champ has not been barking as he usually does and has not been as active. She will like some guidance about why he is not acting like himself. As you have a time slot available this morning and Mrs. Charles lives close, she accepts to bring Champ on her way to work.</p>""",
                "unsafe_allow_html": True,
            },
            "important_details": {
                "type": "text_area",
                "height": 200,
                "label": "List at least three details from this first call with Mrs. Charles that are important to note.",
            }
        },
        "user_prompt": """
Provide me feedback on whether or not I've picked up on at least three distinct and clinically relevant details from the following conversation: 
=============
On a hot, dry March morning, Mrs. Charles called the clinic you are currently working at about Champ. Champ is a young Pothound that Mrs. Charles 
has owned since he was a puppy. She says that Champ has not been barking as he usually does and has not been as active. 
She will like some guidance about why he is not acting like himself. As you have a time slot available this morning and Mrs. 
Charles lives close, she accepts to bring Champ on her way to work.
========================
Provide feedback on whether I've picked up on both environmental and clinical factors that are important to note. 
Here is what I observed: {important_details}.""",
        "ai_response": True,
        "allow_skip": True,
        #"scored_phase": True,
        #"rubric": """
        #    Three details:
        #    3 points - The user provides three key details from the conversation with Mrs. Charles.
        #    2 points - The user provides two key details from the conversation with Mrs. Charles.
        #    1 point - The user provides one key detail from the conversation with Mrs. Charles.
        #    0 points - The user provides no key details from the conversation with Mrs. Charles.
        #""",
        #"minimum_score": 3,
    },
    "discussion_with_mrs_charles": {
        "name": "Discussion with Mrs. Charles",
        "fields": {
            "client_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "https://d2jqdwayv0rru6.cloudfront.net/microapp-images/mrs_chase.webp",
                "caption": "Mrs. Charles arrives with Champ.",
            },
            "arrival_observation": {
                "type": "markdown",
                "body": """<p>When Mrs. Charles arrives with Champ, You observe:</p>
                        <h3>Signalment:</h3>
                        <ul>
                            <li>Champ is a 1 year old dog.</li>
                            <li>Neutered male</li>
                            <li>Pothound</li>
                        </ul>
                        <h3>Presenting Complaint</h3>
                        <ul>
                            <li>Reduced Barking</li>
                            <li>Reduced Activity</li>
                            <li>Not being Himself</li>
                        </ul>
                        <p>Now, you will have a conversation with Mrs. Charles to gather more information about Champ's condition.</p>""",
                "unsafe_allow_html": True,
            },
            "chat_with_mrs_charles": {
                "type": "chat_input",
                "max_messages": 20,
                "placeholder": "[Write your first message to Mrs. Charles...]",
                "initial_assistant_message": "Thanks for seeing Champ, doctor. I've only got a few minutes before I've got to head to work, do you know what is wrong with him?"
            }
        },
        "phase_instructions": """For this chat, you play the role of a 65-year-old woman, Mrs. Charles, living in Grenada. You have brought your dog Champ into the vet clinic.
                                    HEALTH HISTORY:
                                    - Mrs. Charles has had Champ since he was 3 months old, adopted from a shelter.
                                    - Champ is up-to-date on rabies and 5-in-1 vaccine.
                                    - Champ takes Bravecto® every 3 months & Advantage multi® once a month.
                                    ENVIRONMENT:
                                    - Champ is kept outside, in a yard with earth and grass, on a chain.
                                    - He has a small hut in case it rains.
                                    - Only pet, but there's other pets nearby.
                                    - Allowed to roam loose in the neighborhood every few days; often brought on a hash once a month.
                                    DIET:
                                    - Adult dog food twice a day, plus kitchen scraps.
                                    - Water given sporadically; area frequently has water shortages.
                                    MORE DETAILS ABOUT PRESENTING COMPLAINT:
                                    - Decreased activity.
                                    - Not responding to the usual stimuli.
                                    - Reduced barking.
                                    """,
        "user_prompt": "Please summarize my conversation with Mrs. Charles in short bullet points. Write them down in the order they were discovered with no additional analysis or implications outside of what was discussed. Start with 'You write the following notes in your chart based on your conversation with Mrs. Charles:'",
        "ai_response": True,
        "allow_skip": True,
        "rubric": None,
        "scored_phase": False
    },
    "problem_list": {
        "name": "Problem List",
        "fields": {
            "new_problems": {
                "type": "text_area",
                "label": "Now that you've had a consultation with Mrs. Chase, what are two new relevant problems gathered from the signalment, presenting complaint, and/or history.",
                "height": 200,
            }
        },
        "user_prompt": """Provide me feedback on whether or not I've picked up on two new distinct, and clinically relevant details from the interaction so far.  I should list NEW problems that I did not provide in the initial phone call. If I include issues I brought up in the initial phone call. Don't give me credit. 

If I don't provide the details, then don't give me the answer. Just provide the feedback on the items I provide and whether I've picked up on two details. 

Here is what I observed: {new_problems}
""",
        #"rubric": """
        #    1 point - The user provides at least one new key detail from the interaction with Mrs. Charles and Champ that was not picked up during the original phone call.
        #    0 points - The user provides no new key details from the conversation with Mrs. Charles.
        #""",
        #"minimum_score": 1,
        #"scored_phase": True,
        "ai_response": True,
        "allow_skip": True
    },
    "physical_exam": {
        "name": "Physical Exam",
        "fields": {
            "exam_observation": {
                    "type": "markdown",
                    "body": """<p>You turn back to Champ from your notes to start the physical examination. Since he's arrived, you note the following:</p>
                            <ul>
                                <li>Champ is now laying down in sternal recumbency</li>
                                <li>He is QAR (quiet, alert and responsive), looks slightly lethargic.</li>
                                <li>Panting</li>
                            </ul>""",
                    "unsafe_allow_html": True,
                },
                "champ_image": {
                    "type": "image",
                    "decorative": True,
                    "width": 300,
                    "image": "https://d2jqdwayv0rru6.cloudfront.net/microapp-images/champ2.webp",
                    "caption": "Champ is now laying down in sternal recumbency",
                }
            },
        "button_label": "Perform Physical Exam",
        "ai_response": False,
        "custom_response": """You perform the physical examination and observe the following:
                        
-   **Weight:** 25 lbs
-   **BCS:** 4/9
-   **Rectal Temperature:** 100 F / 37.8 C (Reference interval: 99.5-102.5F or 37.5-39.2C)
-   **Pulse:** 110 bpm (Reference interval: 90-120 bpm)
-   **Respiratory Rate:** Panting
-   **Mucous Membranes:** Pink, tacky
-   **CRT:** 2 seconds
-   **Eyes:** Corneas clear, pupils normal size, symmetrical, sclera white, no ocular discharge. Eye globes seem slightly retracted.
-   **Ears:** No exudate observed, no redness present.
-   **Oral Cavity:** Teeth are free from excessive tartar, no gingivitis present.
-   **Nose:** No obvious abnormalities observed.
-   **Heart:** Regular rhythm; no murmur detected.
-   **Pulse Quality:** Synchronous with heartbeat, strong.
-   **Skin Tent:** Prolonged.
-   **Respiratory:** Lungs auscultate clear on four quadrants bilaterally; trachea clear. No wheezes or crackles noted.
-   **Abdomen:** Abdomen palpates normally; no pain.
-   **Urogenital:** External genitalia appears normal; small palpable bladder.
-   **Lymph Nodes:** All normal in size.
-   **Skin:** Normal amount of shedding; skin looks normal; hair coat in good condition.
-   **Musculo-Skeletal:** No apparent abnormalities.
-   **Neurological:** No apparent abnormalities.""",
        "rubric": None,
        "scored_phase": False,
        "allow_skip": True
    },
    "clinical_exam_findings": {
        "name": "Clinical Exam Findings",
        "fields": {
            "pink_mucous_membranes": {
                "type": "radio",
                "label": "Pink mucous membranes",
                "options": ['normal', 'problematic']
            },
            "tacky_mucous_membranes": {
                "type": "radio",
                "label": "Tacky mucous membranes",
                "options": ['normal', 'problematic']
            },
            "skin_tent": {
                "type": "radio",
                "label": "Skin tent",
                "options": ['normal', 'problematic']
            },
            "temperature": {
                "type": "radio",
                "label": "Temperature",
                "options": ['normal', 'problematic']
            },
            "lethargic": {
                "type": "radio",
                "label": "Lethargic",
                "options": ['normal', 'problematic']
            },
            "abdominal_palpitation": {
                "type": "radio",
                "label": "Abdominal Palpitation",
                "options": ['normal', 'problematic']
            },
            "crts": {
                "type": "radio",
                "label": "CRT=2s",
                "options": ['normal', 'problematic']
            },
            "lungs": {
                "type": "radio",
                "label": "Lungs auscultate clear on four quadrants bilaterally",
                "options": ['normal', 'problematic']
            },
            "qar": {
                "type": "radio",
                "label": "QAR (quiet, alert and responsive)",
                "options": ['normal', 'problematic']
            },
            "pulse": {
                "type": "radio",
                "label": "Strong, synchronous femoral pulse:",
                "options": ['normal', 'problematic']
            },
            "panting": {
                "type": "radio",
                "label": "Panting",
                "options": ['normal', 'problematic']
            },
            "heart_rate": {
                "type": "radio",
                "label": "Heart Rate",
                "options": ['normal', 'problematic']
            },
            "eyes": {
                "type": "radio",
                "label": "Eye globes slightly retracted",
                "options": ['normal', 'problematic']
            },
        },
        "user_prompt": """Please provide feedback on my answers vs the answer key. Prioritize by individually listing the answers I got incorrect at the top and why my answer is incorrect. Then you can provide generic feedback or encouragement (not a list) for the answers I got right. 
                        ## Answer key: 

                        ### Important Issues: 
                        Tacky mucous membranes: they should be moist so this is a problem. 
                        Skin tent: this is a problem: skin tent is delayed, skin should be elastic and come back quickly into normal position after pinch. 
                        Lethargic: this is a problem
                        Abdominal palpation: this is normal
                        QAR (quiet, alert and responsive): Quietness can be a problem especially if Champ is normally excited –it can be another sign of lethargy 
                        Eye globes slightly retracted: this is a problem

                        ### Could be Important or Normal
                        Panting: this is not necessarily a problem, especially if rectal temperature is normal?

                        ### Normal (non-important) Factors
                        Pink mucous membranes: this is normal
                        Temperature: this is normal
                        CRT=2s : this is normal
                        Lungs auscultate clear on four quadrants bilaterally: this is normal
                        Strong, synchronous femoral pulse: this is normal
                        HR: this is normal. 
                        
                        My observations: 
                        Pink Mucous Membranes: {pink_mucous_membranes}
                        Tacky Mucous Membranes: {tacky_mucous_membranes}
                        Skin Tent: {skin_tent}
                        Temperature: {temperature}
                        Lethargy: {lethargic}
                        Abdominal Palpitation: {abdominal_palpitation}
                        CRTs: {crts}
                        Lungs: {lungs}
                        QAR: {qar}
                        Pulse: {pulse}
                        Panting: {panting}
                        Heart Rate: {heart_rate}
                        Eyes: {eyes}
                    """,
            "rubric": None,
            "scored_phase": False,
            "allow_skip": True
        },
        "diagnosis": {
            "name": "Diagnosis",
            "fields": {
                "diagnosis": {
                    "type": "radio",
                    "label": "Do you believe that Champ is dehydrated, hypovolemic, or both?",
                    "options": ["Dehydration", "Hypovolemia", "Both dehydration and hypovolemia"]
                },
                "diagnosis_explanation": {
                    "type": "text_area",
                    "label": "Explain your diagnosis.",
                    "height": 200,
                }
            },
            "user_prompt": """Here is my diagnosis: {diagnosis}
            And explanation: {diagnosis_explanation}
            Provide me feedback on my diagnosis of Dehydration, Hypovolemia, or both. Explain to me where, if applicable, my reasoning is accurate based on the facts of the case. Explain to me where, if applicable, my reasoning is inaccurate based on the facts of the case. 
            """,
            "rubric": None,
            "scored_phase": False,
            "allow_skip": True
        }
}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {
    "temperature": 0.7
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You have reached the end! I hope you learned something new!"
COMPLETION_CELEBRATION = False

PAGE_CONFIG = {
    "page_title": "Case Study: Champ the Sunbathing Dog",
    "page_icon": "🐶",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

USE_SQL = False
USE_GSHEETS = False

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())