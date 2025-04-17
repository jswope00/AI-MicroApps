PUBLISHED = False
APP_URL = "https://voting-decision-tree.streamlit.app"

APP_TITLE = "Hang a Picture"
APP_INTRO = """This app helps you hang a painting, framed photo, or other flat artwork on the wall of a home or gallery"""

APP_HOW_IT_WORKS = """
This app helps you hang a picture by telling you where to hammer your nail based on the size of your wall and the frame.\n\nIt uses OpenAI behind the scenes to calculate this position based on the fields you complete and generates instructions accordingly. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    "button_text": "Make your own AI MicroApp",
    "url": "https://www.youtube.com/watch?v=jqpEJ2995IA"    
}

SYSTEM_PROMPT = """Acting as an expert in curating displays of art in homes, galleries, and museums, you will generate concise instructions in plain language understandable by a lay person on how to hang a picture, specifically where to place a nail in accordance with the measurements of the wall and picture supplied in the prompt. You may also mention tips such as placing painter's tape on the wall where you plan to drill or hammer to prevent the wall from chipping and making dust."""

PHASES = {
   "dimension_calculations": {
        "name": "Calculate your nail's position",
        "fields": {
            "info": {
                "type": "markdown",
                "body": "Use a tape measure to find the following dimensions."
            },
            "measurement-units": {
                "type": "selectbox",
                "options": ['inches', 'centimeters'],
                "label": "Are you measuring dimensions in inches or centimeters?",
                "help": "Whole numbers without fractions or decimals will suffice",
            },
            "viewer-height-inches": {
                "type": "slider",
                "min_value": 60,
                "max_value": 75,
                "label": "How tall is your average viewer in inches? (The average American height is 66 in.)",
                "showIf": {"measurement-units": "inches"},
            },
            "viewer-height-cm": {
                "type": "slider",
                "min_value": 155,
                "max_value": 180,
                "label": "How tall is your average viewer in centimeters? (The average American height is 168 cm.)",
                "showIf": {"measurement-units": "centimeters"},
            },
            "picture-height": {
                "type": "number_input",
                "step": 1,
                "label": "What's the height of your picture, including the frame?",
            },
            "drop-to-hardware": {
                "type": "number_input",
                "step": 1,
                "label": "How far below the top of the picture is the hanger on the back?",
                "help": "Measure down from the top to the place where the nail will go, whether a hook or a wire held taut, in the units you chose (inches or cm).",
            },
            "available_wall_width": {
                "type": "number_input",
                "step": 1,
                "label": "How much horizontal wall space is available?",
                "help": "Include the total span in the units you chose (inches or cm), eg between adjacent walls, nearby furniture, or pictures to the left and right.",
            },
            "picture-weight": {
                "type": "selectbox",
                "options": ['light (under 5 pounds)', 'medium (5-20 pounds)', 'heavy (over 20 pounds)'],
                "label": "How heavy is the picture?",
                "help": "Include the frame and glazing, if any"
            },
            "wall-type": {
                "type": "selectbox",
                "options": ['normal', 'reinforced'],
                "label": "What type of wall are you hanging on?",
                "help": "Most buildings have normal drywall, but some galleries are reinforced with plywood backing"
            },
        },
        "user_prompt": [
            {
                "condition": {},
                "prompt": "Please use \"{measurement-units}\" in all of your output for this prompt."
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
    "page_title": "Hang a Picture",
    "page_icon": "️🖼",
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
