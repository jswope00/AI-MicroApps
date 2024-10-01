APP_TITLE = "Evaluation Draft Feedback"
APP_INTRO = """This is a template for an AI-powered Microapp that scores a learner's evaluation draft against a checklist."""

APP_HOW_IT_WORKS = """
This AI-Powered Microapps work by scoring the learner input against the checklist. 

Please review the provided evaluation draft and provide feedback based on the following rubric.
Rubric:
**Done well: The item fully addresses the criterion.
**Needs improvement: The item partially addresses the criterion.
**Not included: The item does not address the criterion.
Criteria to be scored:
**Does the evaluation have process objectives but more so have outcome objectives?
**Is who will conduct the evaluation named and tell how they were selected?
**Does each objective have a definition of what success would look like?
**Does the evaluation methodology describe what data will be collected and how?
**Is there an industry standard process used to evaluation the data?
**How will the findings be used to improve the next phase of the project?
**Does the evaluation plan state how findings will be reported out and to whom?


 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = "Please review the provided evaluation draft and provide feedback according to the following rubric. Prioritize the feedback you provide based on the rubric but don't show the user the rubric or any score give."

PHASES = {
    "phase1": {
        "name": "Evaluation Draft",
        "fields": {
            "evaluation_draft": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste your Evaluation Draft""",
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
            1. Does the evaluation have process objectives but more so have outcome objectives?
            2. Is who will conduct the evaluation named and tell how they were selected?
            3. Does each objective have a definition of what success would look like?
            4. Does the evaluation methodology describe what data will be collected and how?
            5. Is there an industry standard process used to evaluation the data?
            6. How will the findings be used to improve the next phase of the project?
            7. Does the evaluation plan state how findings will be reported out and to whom?

            
        Provide a paragraph stating what they did well and feedback for only two criteria that could be improved.

        **Text:**
        {evaluation_draft}
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

COMPLETION_MESSAGE = "You've reached the end! I hope this feedback helps you to review your evaluation draft. Be sure to continue to refine before you submit."
COMPLETION_CELEBRATION = False