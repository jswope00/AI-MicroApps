APP_TITLE = "Essay Scoring"
APP_INTRO = """
"""

APP_HOW_IT_WORKS = """
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You score student's text snippets according to a rubric."""

PHASES = {
    "phase1": {
        "name": "Lead",
        "fields": {
            "lead": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste the LEAD""",
                "value": "Modern humans today are always on their phone. They are always on their phone more than 5 hours a day no stop .All they do is text back and forward and just have group Chats on social media. They even do it while driving. "
            }
        },
        "phase_instructions": "",
        "user_prompt": """Simply read my text and provide brief feedback and a score based on the following rubric: 
        Rubric: 
            2 points - Effective: The lead grabs the reader's attention and strongly points toward the position. For example, for the prompt "Should we admire heroes but not celebrities", the response "Too often in today's society people appreciate only the circumstances which immediately profit themselves and they follow the pack, never stopping to wonder, 'Is this really the person who deserves my attention?'" would be effective. 
                1 points - Adequate: The lead attempts to grab the reader's attention and points toward the position. For example, for the prompt "Prompt: "Can people ever be truly original?" the response "Originality: being able to do something that few or none have done before." would be adequate. 
                0 points - Ineffective: The lead may not grab the readers' attention and may note point to the position. For example, for the prompt "Prompt: "Can people ever be truly original?" The response" Originality is hard to in this time and era." would be ineffective.

                Text: 
                {lead}
                """,
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
            1. LEAD
                2 points - Effective: The lead grabs the reader's attention and strongly points toward the position. For example, for the prompt "Should we admire heroes but not celebrities", the response "Too often in today's society people appreciate only the circumstances which immediately profit themselves and they follow the pack, never stopping to wonder, 'Is this really the person who deserves my attention?'" would be effective. 
                1 points - Adequate: The lead attempts to grab the reader's attention and points toward the position. For example, for the prompt "Prompt: "Can people ever be truly original?" the response "Originality: being able to do something that few or none have done before." would be adequate. 
                0 points - Ineffective: The lead may not grab the readers' attention and may note point to the position. For example, for the prompt "Prompt: "Can people ever be truly original?" The response" Originality is hard to in this time and era." would be ineffective.
        """,
        "minimum_score": 0,
        "show_prompt": True
    }
    

}

PREFERRED_LLM = "gpt-4-turbo"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
