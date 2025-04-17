APP_URL = "https://clinical-feedback.streamlit.app"
PUBLISHED = True
APP_IMAGE = "clinical_feedback_flat.webp"

##AREAS OF FOCUS from https://asmepublications-onlinelibrary-wiley-com.sgu.idm.oclc.org/doi/epdf/10.1111/tct.13766 "Making Narrative Feedback Meanignful""

# " narrative feedback frequently does not providethe level of specificity to reinforce strong performance and correctmistakes, leaving students dissatisfied with the feedback received."
# " Our approach wasgrounded in feedback principles linked to the deliberate practiceframework with educational interventions designed to change behav-iours based on the social cognitive theory""
# """Good feedback includes the following: """"
# - Positive Feedback that is specific
# - Constructive Feedback that is specific
# - Improvement Plan that is specific and actionable. 

# This article: Improving the quality of written feedback using written feedback (https://eprints.whiterose.ac.uk/103779/3/ImprovingQualityWrittenFeedback.pdf)
# - EPs should contain clear descriptions of what students did well and clear statements of the areas for improvement, 
# - Statements should be linked to observed behaviours at the level of the **task** rather than the self
# - Both (what students did well and areas for improvement) should be anchored in specific consultations to aid recall and emphasise the relevance of the feedback to real clinical practice; building ‘logical connections’ for students
# - The numbers of identified strengths and areas for improvement should be limited and prioritised so that students can focus their efforts to improve in the most important areas identified in the verbal discussion;



APP_TITLE = "Clinical Scenario Feedback Generator"
APP_INTRO = """This application generates feedback in narrative form based on numeric scores from a clinical feedback scenario. 
"""

APP_HOW_IT_WORKS = """
 This is an **AI-Powered Feedback Generator ** that writes narrative feedback for a simulated patient scenario based on a numeric rubric. It is prompted to provide positive and constructive feedback that is specific. And to provide improvement plans that are specific and actionable.
 Sample text is fed to the AI, so the chance of hallucination is less likely. Conversely, the AI only has general statements and numeric inputs so it does not have the data to point to specific, observeable behaviors from the student's interaction. 
threshold for each question. The threshold could be as low as zero points to pass any answer, or it could be higher. 

Using AI to provide feedback and score like this is a very experimental process. Some things to note: 

 - AIs make mistakes. Users are encourage to skip a question if the AI is not understanding them or giving good feedback. 
 - The AI might say things that it can't do, like "Ask me anything about the article". I presume further refinement can reduce these kinds of responses. 
 - Scoring is highly experimental. At this point, it should mainly be used to gauge if a user gave an approximately close answer to what the rubric suggests. It is not recommended to show the user the numeric score. 
 - Initial testing indicates that the AI is a very easy grader. This is probably good in this experiment, and it may be refined with different prompting. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    "url":"https://asmepublications-onlinelibrary-wiley-com.sgu.idm.oclc.org/doi/epdf/10.1111/tct.13766",
    "button_text":"View Study"
}

SYSTEM_PROMPT = "You provide narrative written feedback to students in a simulated pateient scenario based on a numeric rubric and suggested dialogue. You aim to provide positive and constructive feedback that is specific. And you provide improvement plans that are specific and actionable.  "

PHASES = {
    "phase1": {
        "name": "Clinical Feedback",
        "fields": {
            "exam_name": {
                "type": "text_input",
                "label": "Exam Name",
                "value": "PCM501 CLINICAL SKILLS",
                "key": "exam_name"
            },
            "priorities": {
                "type": "number_input",
                "label": "Negotiates priorities & sets agenda",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "priorities"
            },
            "timeline": {
                "type": "number_input",
                "label": "Timeline",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "timeline"
            },
            "organization": {
                "type": "number_input",
                "label": "Organization",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "organization"
            },
            "transition": {
                "type": "number_input",
                "label": "Transitional statement",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "transition"
            },
            "question_types": {
                "type": "number_input",
                "label": "Questioning skills – types of questions",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "question_types"
            },
            "question_relevance": {
                "type": "number_input",
                "label": "Questioning skills – Relevance and Content",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "question_relevance"
            },

            "question_summarizing": {
                "type": "number_input",
                "label": "Questioning Skills – Summarizing",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "question_summarizing"
            },
            "question_verification": {
                "type": "number_input",
                "label": "Questioning Skills – Verification of Patient Information",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "question_verification"
            },
            "support_systems": {
                "type": "number_input",
                "label": "Support Systems",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "support_systems"
            },
            "education": {
                "type": "number_input",
                "label": "Patient’s Education & Understanding",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "education"
            },
            "consent": {
                "type": "number_input",
                "label": "Informed Consent for Investigations & Procedures",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "consent"
            },
            "shared_plan": {
                "type": "number_input",
                "label": "Achieve a Shared Plan",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "shared_plan"
            },
            "closure": {
                "type": "number_input",
                "label": "Closure",
                "min_value": 0,
                "max_value": 4,
                "value": 2,
                "step": 1,
                "key": "closure"
            }
        },
        "phase_instructions": "I will rewrite narrative clinical feedback according to instructions provided. Please provide me with instructions.",
        "user_prompt": "Please rewrite the following narrative clinical feedback for a medical student who has completed a clinical scenario. Organize the feedback into positive aspects first, followed by areas for improvement. Use depersonalized language and passive voice",
        "ai_response": False,
        "custom_response": "Welcome {name} and Thanks for providing your background in the study as {background}.",
        "scored_phase": False,
        "allow_revisions": False,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
}

def generate_prompt(config):
    exam_name = config.get("exam_name", "")
    
    feedback = {
        "positive": [],
        "improvement": []
    }
    
    criteria = {
        "priorities": {
            "positive": "Excellent job exploring all matters affecting the patient and involving them in addressing these issues.",
            "improvement": "The patient may have other concerns in addition to the chief complaint. If it is an extensive list, then the issues can be ranked. Aim to explore all matters affecting the patient and involve the patient in the plan for addressing all these issues."
        },
        "timeline": {
            "positive": "Well done establishing a clear chronology of the clinical presentation.",
            "improvement": "Patients tend to present with a multitude of symptoms. Ensure you ask the relevant questions to establish a chronology of the clinical presentation. This helps to establish a disease course."
        },
        "organization": {
            "positive": "Excellent organization of data gathering. Questions were asked in a logical sequence, focusing on one topic before moving to another.",
            "improvement": "Your data gathering seems disorganized. Try to ask questions on one topic before exploring another."
        },
        "transition": {
            "positive": "Effective use of transitional statements throughout the interview, smoothly guiding the patient through different topics and preparing them for what comes next.",
            "improvement": "The use of transitional statements can be a valuable communication technique. It alerts the patient to what is coming next. For example, \"I'd like to ask you some personal questions. I ask these from all my patients, and I will keep your answers confidential.\""
        },
        "question_types": {
            "positive": "Skillful use of various question types, starting with open-ended questions and following up with specific inquiries. This approach effectively encouraged the patient to share information.",
            "improvement": "When asking questions from patients, begin with an open-ended question, followed by more specific questions. Limit the use of why questions and leading questions. The aim is to encourage the patient to talk."
        },
        "question_relevance": {
            "positive": "Thorough exploration of symptoms associated with the chief complaint, effectively eliciting both pertinent positives and negatives to aid in formulating differential diagnoses.",
            "improvement": "Symptoms do not occur in isolation. It is imperative to elicit the presence and absence of symptoms associated with the chief complaint to aid in formulating differential diagnoses."
        },
        "question_summarizing": {
            "positive": "Excellent use of summarization techniques before concluding the patient encounter, allowing for verification of accuracy and completeness of information gathered.",
            "improvement": "Summarization is a valuable communication technique to do before completing the patient encounter. It allows patients to check for accuracy. The physician also benefits since it serves as a review for clarity and completeness."
        },
        "question_verification": {
            "positive": "Consistently sought verification and clarity for ambiguous patient responses, ensuring accurate understanding of the patient's situation.",
            "improvement": "Aim to seek verification and clarity whenever there are ambiguous patient responses."
        },
        "support_systems": {
            "positive": "Comprehensive investigation of the patient's support systems, including finances and resources available. Excellent assessment of the patient's access to healthcare.",
            "improvement": "You did not investigate the patient's support systems. You have to determine the finances and other resources available to the patient. Furthermore, feasibility for access to healthcare must be determined."
        },
        "education": {
            "positive": "Effective use of techniques such as 'teach-back' and hypothetical scenarios to check and ensure patient understanding of information provided.",
            "improvement": "Aim to check patient understanding of information. Techniques include \"teach-back,\" posing hypotheticals."
        },
        "consent": {
            "positive": "Thorough explanation of diagnostic investigations and procedures, clearly communicating risks, benefits, alternatives, and potential consequences of refusal.",
            "improvement": "Diagnostic investigations and procedures play an essential role in patient management- screening, diagnosis, monitoring, prognosis. The patient must understand the risks, benefits, alternatives of these, and the consequences of refusal."
        },
        "shared_plan": {
            "positive": "Excellent discussion of diagnosis and prognosis, actively encouraging patient participation in the plan. This approach likely increased patient satisfaction, understanding, empowerment, and responsibility.",
            "improvement": "Diagnosis and prognosis must be discussed in detail. The patient must be encouraged to participate in this plan, for example, sharing their thoughts. This increases patient satisfaction, understanding, empowerment, responsibility."
        },
        "closure": {
            "positive": "Clear and comprehensive closure of the interview, including a well-explained shared plan for the future and appropriate discussion of follow-up needs. Both physician and patient responsibilities were clearly outlined.",
            "improvement": "The physician must inform the patient about their shared plan for the future at the end of the interview. The need or no need for follow-up must be discussed and arranged. Both physician and patient must be cognizant of their responsibilities."
        }
        # ... (continue for all other criteria)
    }
    
    for criterion, messages in criteria.items():
        score = config.get(criterion, 0)
        if score >= 3:
            feedback["positive"].append(f"[{criterion}_positive] {messages['positive']}")
        else:
            feedback["improvement"].append(f"[{criterion}_improvement] {messages['improvement']}")
    
    intro = f"Patient History Taking and Management are essential responsibilities of a physician. This e-mail provides feedback on the communication and interpersonal skills portion of your {exam_name} exam.\n\n"
    
    positive_feedback = "\n".join(feedback["positive"]) if feedback["positive"] else "No specific positive feedback provided."
    improvement_feedback = "\n".join(feedback["improvement"]) if feedback["improvement"] else "No specific areas for improvement identified."
    
    prompt = f"""
Please rewrite the following narrative clinical feedback for a medical student who has completed a clinical scenario. Organize the feedback into positive aspects first, followed by areas for improvement. Use depersonalized language and passive voice:

Positive Feedback:
{positive_feedback}

Areas for Improvement:
{improvement_feedback}

Please format your response using the following template:

{intro}

[Brief narrative summary of positive feedback, provided in paragraph format, no more than three sentences. You do not have to incorporate all the positive feedback attributes. Not a bullet list]

Areas for Improvement:
- [Area 1]
- [Area 2]
...

Conclusion:
[A brief summary of the student's performance and an Improvement Plan that is specific and actionable]
"""
    
    return prompt

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = True
SOURCE_DOCUMENT = "sample.pdf"

PAGE_CONFIG = {
    "page_title": "Clinical Feedback",
    "page_icon": "️💊",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())