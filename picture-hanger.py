PUBLISHED = False
APP_URL = "https://voting-decision-tree.streamlit.app"

APP_TITLE = "How To Vote: A Decision Tree Generator for College Students"
APP_INTRO = """This app helps you draw a custom flowchart to help your students decide when and where to vote. 
"""

APP_HOW_IT_WORKS = """
A simple flowchart can help students overwhelmed with classes fit voting into their schedule. This app tries to draw a custom decision tree based on a teacher's answers to a few fields.\n\nIt utilizes the OpenAI and other AI APIs to send a custom prompt to AI with the user's inputs and returns the AI's response. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    "button_text": "BallotPedia.org Sample Ballot",
    "url": "https://ballotpedia.org/wiki/index.php?title=Sample_Ballot_Lookup&Source=sitenotice"    
}



SYSTEM_PROMPT = """Acting as an expert in data visualization, you will generate the code required to draw a decision tree. You must use the syntax for the Mermaid.js JavaScript library to produce the visualization. Do not create an image directly with a text-to-image generator like DALL-E; it must be constructed with the markdown-like Mermaid.js code."""

PHASES = {
   "tree-generation": {
        "name": "Build your Voting Decision Chart",
        "fields": {
            "info": {
                "type": "markdown",
                "body": "Select the options that your students have available to them to generate a shareable voting decision tree. Students should have at least the option to vote at home, on-campus, or off-campus in order for the tool to generate results."
            },
            "hometown-option": {
                "type": "checkbox",
                "label": """My students have enough time to vote at home.""",
                "help": "If so, the flowchart will give them the option to vote in their hometowns.",
            },
            "absentee-option": {
                "type": "checkbox",
                "label": """My students have enough time to order an absentee ballot.""",
                "help": "If checked, the flowchart will offer that option.",
            },
            "oncampus-option": {
                "type": "checkbox",
                "label": """My students can vote on-campus.""",
                "help": "This assumes there's one or more designated campus facilities.",
            },
            "oncampus-locations": {
                "type": "text_input",
                "label": """Where can students vote on-campus?""",
                "help": "Give one or more times and/or addresses. Short answers fit the flowchart best!",
                "value": "9am-5pm in 123 Susan B. Anthony Hall",
            },
             "oncampus-requirements": {
                "type": "text_input",
                "label": """What must students do to vote on campus?""",
                "help": "Mention any requirements for voting in that location.",
                "value": "Bring a photo id and proof of residency",
            },
            "offcampus-option": {
                "type": "checkbox",
                "label": """Students can vote off-campus in nearby town/s.""",
                "help": "If checked, the flowchart will offer that option.",
            },
            "offcampus-locations": {
                "type": "text_input",
                "label": """Where can students vote off-campus?""",
                "help": "Give one or more times and/or addresses. Short answers fit the flowchart best!",
                "value": "9am-5pm at the Springfield Town Hall, 789 Main Street",
            },
              "offcampus-requirements": {
                "type": "text_input",
                "label": """What must students do to vote off campus?""",
                "help": "Mention any requirements for voting in that location.",
                "value": "Bring a photo id and proof of residency",
            },
        },
        "user_prompt": [
            {
                "condition": {},
                "prompt": "Please generate mermaid.js code with a decision tree for voting. Here are the steps in order."
            },
            {
                "condition": {},
                "prompt": "- Start off by asking if the user wants to vote. If no, then tell them thank you and end the branch. If yes, then provide the following options:\n",
            },
            {
                "condition": {"$or":[{"hometown-option": True},{"absentee-option": True}]},
                "prompt": "- Ask if the user wants to vote on hometown issues. If yes, then ask if they have time to go home. If the student has time to go home, then this branch stops with 'Go home and vote. Check 'ballotpedia.org' for local voting information.' If the student does not have time, then end this branch with 'Request an absentee ballot'.\n",
            },
            {
                "condition": {"oncampus-option": True},
                "prompt": "Vote on campus.\n End the branch with a box that includes \"{oncampus-locations}\" and \"{oncampus-requirements}\"\n",
            },
            {
                "condition": {"offcampus-option": True},
                "prompt": "Vote off campus.\n End the branch with a box that includes \"{offcampus-locations}\" and \"{offcampus-requirements}\"\n",
            },
            {
                "condition": {},
                "prompt": """Once you have shared the Mermaid.js code to generate this flowchart, tell the user to paste in into the Mermaid live editor, and give the user a link to https://mermaid.live. Also tell the user that non-partisan information about candidates and issues on their ballot can be found at Ballotpedia, and give them a link to https://ballotpedia.org/wiki/index.php?title=Sample_Ballot_Lookup&Source=sitenotice with a recommendation to type their zip code into the search box."""
            },
          ],
        "ai_response": True,
        "allow_skip": False,
        "show_prompt": True,
        "allow_revisions": True,
        #"read_only_prompt": False
    }
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {"gpt-4o-mini": {
        "family": "openai",
        "model": "gpt-4o-mini",
        "max_tokens": 1000,
        "temperature": 1.0,
        "top_p": 1.0,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "supports_image": False,
        "price_input_token_1M": 0.15,
        "price_output_token_1M": 0.60
    }
}

PAGE_CONFIG = {
    "page_title": "Voting Decision Tree",
    "page_icon": "️✅",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

SIDEBAR_HIDDEN = True

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "⚠️ Chatbots can generate incorrect results; always check the output before publishing it. We hope this app makes voting easier!"
COMPLETION_CELEBRATION = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
