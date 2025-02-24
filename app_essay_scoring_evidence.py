PUBLISHED = False
APP_URL = "https://ai-essay-scoring-demo.streamlit.app"

APP_TITLE = "Essay Scoring - Evidence"
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
            "claim": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste the CLAIM""",
                "value": "Drivers who used their phone while operating a vehicle are most likely to get into an accident that could be fatal. "
            },
            "evidence": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste the EVIDENCE""",
                "value": "According to an article by the Edgar Snyder Firm, 21% of teens that were part of a fatal car accident was due to phones. According to the same article, 35% know the risk but continue using their phones while on the road. This shows that its beyond dangerous and irresponsible of drivers not to be fully aware of their surroundings while driving. Drivers should be able to concentrate without any distractions, because it could be fatal. According to another article, 'Distracted Driving' by the NHTSA, there has already been about 3,000 phone related car accident deaths since 2017. The article states that teen get too distracted with their phones, which causes their accident. Accidents that can be easily avoided by focusing on the road and not a phone. Drivers should not be able to use their phones at all while driving. "
            }
        },
        "phase_instructions": "",
        "user_prompt": """Simply read my text and provide brief feedback and a score based on the following rubric: 
        Rubric: 
            2 points - Effective: The evidence is closely relevant to the claim they support and back up the claim objectively with concrete facts, examples, research, statistics, or studies. The reasons in the evidence support the claim and are sound and well substantiated. For example, for the claim 'There are a number of instances, in either our everyday lives or special occurrences, in which one must confront an issue they do not want to face.' the evidence 'For instance, the presidential debate is currently going on and in order to choose the right candidate, they must research all sides of both candidates. The voter must learn all about the morals and how each one plans to better America. This might disturb some people, given that some people may either feel too strongly about a certain candidate or that they may not feel strongly enough. However, by not researching and gaining all the possible knowledge that they can, they are hurting themselves by passing up a valuable opportunity to possibly better the country for themselves and the people surrounding them' would be effective.
                1 points - Adequate: The evidence is not closely relevant to the claim it supports. The evidence contains some detailed examples but they may not be relevant to each other and only loosely bound together. The evidence uses some unsubstantiated or unsound claims or assumptions. For example, for the claim 'Individuals do not have an obligation to others to think seriously about important matters' the evidence 'It is never fair for an individual to place their beliefs or state of mind onto someone else. An individual never knows where someone else might be in their life, and in result the individual cannot and should not force anything onto them.' would be adequate. 
                0 points - Ineffective: The evidence is irrelevant to the claim it backs up and provide few valid examples. The evidence uses unsubstantiated assumptions that sound quite unacceptable. For example, for the claim 'I feel like it is pretty much part of the human rights.' the evidence 'We cannot, not allow someone just to think, even if we know that doing is maybe difficult. Imagine that, what if somebody came up a brilliant idea in a really difficult case, but that person doesn't have enough power to make it happen, but another person has. So if he tells it to the other one, he can make it happen. This way they can help each other out, and that is how society can take a step ahead.' is ineffective.

                My claim is: 
                {claim}

                My evidence is:
                {evidence}
                """,
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
        Evidence:
            2 points - Effective: The evidence is closely relevant to the claim they support and back up the claim objectively with concrete facts, examples, research, statistics, or studies. The reasons in the evidence support the claim and are sound and well substantiated. For example, for the claim 'There are a number of instances, in either our everyday lives or special occurrences, in which one must confront an issue they do not want to face.' the evidence 'For instance, the presidential debate is currently going on and in order to choose the right candidate, they must research all sides of both candidates. The voter must learn all about the morals and how each one plans to better America. This might disturb some people, given that some people may either feel too strongly about a certain candidate or that they may not feel strongly enough. However, by not researching and gaining all the possible knowledge that they can, they are hurting themselves by passing up a valuable opportunity to possibly better the country for themselves and the people surrounding them' would be effective.
            1 points - Adequate: The evidence is not closely relevant to the claim it supports. The evidence contains some detailed examples but they may not be relevant to each other and only loosely bound together. The evidence uses some unsubstantiated or unsound claims or assumptions. For example, for the claim 'Individuals do not have an obligation to others to think seriously about important matters' the evidence 'It is never fair for an individual to place their beliefs or state of mind onto someone else. An individual never knows where someone else might be in their life, and in result the individual cannot and should not force anything onto them.' would be adequate. 
            0 points - Ineffective: The evidence is irrelevant to the claim it backs up and provide few valid examples. The evidence uses unsubstantiated assumptions that sound quite unacceptable. For example, for the claim 'I feel like it is pretty much part of the human rights.' the evidence 'We cannot, not allow someone just to think, even if we know that doing is maybe difficult. Imagine that, what if somebody came up a brilliant idea in a really difficult case, but that person doesn't have enough power to make it happen, but another person has. So if he tells it to the other one, he can make it happen. This way they can help each other out, and that is how society can take a step ahead.' is ineffective.
    """,
        "minimum_score": 0,
        "show_prompt": True
    }
    

}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Essay Scoring",
    "page_icon": "🔤️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())