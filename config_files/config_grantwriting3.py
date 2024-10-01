APP_TITLE = "Problem Statement Feedback"
APP_INTRO = """This is a template for an AI-powered Microapp that scores a learner's problem statement draft against a checklist."""

APP_HOW_IT_WORKS = """
This AI-Powered Microapps work by scoring the learner input against the checklist. 

Please review the provided problem statement draft and provide feedback based on the following rubric.
Rubric:
**Done well: The item fully addresses the criterion.
**Needs improvement: The item partially addresses the criterion.
**Not included: The item does not address the criterion.
Criteria to be scored:
**Does the proof of problem or need connect to the purpose of the organization?
**Does this component provide statistical evidence?
**Is the information coming from credible sources?
**Is the content informed by clientele or beneficiaries?
**Does it avoid stating 'lack of method' as a reason for addressing the issue?
**Does it avoid making assumptions?
**Does it use jargon that many reviewers wouldn’t understand?

 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = "Please review the provided problem statement draft and provide feedback according to the following rubric. Prioritize the feedback you provide based on the rubric but don't show the user the rubric or any score give."

PHASES = {
    "phase1": {
        "name": "Problem Statement",
        "fields": {
            "problem_statement": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste your Problem Statement draft""",
                "value": ""
            }
        },
        "phase_instructions": "",
        "user_prompt": """Simply read my text and provide brief feedback and a score based on the following rubric:
        
        **Rubric:**
            2 points - Done well: The item fully addresses the criterion.
            1 point - Needs improvement: The item partially addresses the criterion.
            0 points - Not included: The item does not address the criterion.
            
        **Criteria to be scored:**
            1. Does the proof of problem or need connect to the purpose of the organization?
            2. Does this component provide statistical evidence?
            3. Is the information coming from credible sources?
            4. Is the content informed by clientele or beneficiaries?
            5. Does it avoid stating 'lack of method' as a reason for addressing the issue?
            6. Does it avoid making assumptions?
            7. Does it use jargon that many reviewers wouldn’t understand?
            
        Provide a paragraph stating what they did well and feedback for only two criteria that could be improved.

        **Text:**
        {problem_statement}
        """,
        "allow_skip": False,
       
    }
}




PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

INITIAL_SIDEBAR_STATE = "collapsed"  # Options: "auto", "expanded", "collapsed"

SIDEBAR_HIDDEN = True

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope this feedback helps you to review your problem statement. Be sure to continue to refine before you submit."
COMPLETION_CELEBRATION = False