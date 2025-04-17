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

SYSTEM_PROMPT = """Acting as an expert in curating displays of art in homes, galleries, and museums, you will generate concise instructions in plain language understandable by a lay person on how to hang a picture, specifically where to place a nail in accordance with the measurements of the wall and picture supplied in the prompt. You'll calculate the EYE_HEIGHT = .93 * VIEWER_HEIGHT. For the nail's height off the floor, use the formula NAIL_HEIGHT = EYE_HEIGHT + (PICTURE_HEIGHT/2) - DROP_TO_HARDWARE. For the nail's distance from the nearest horizontal obstacle, use the formula NAIL_HORIZONTAL_POSITION = AVAILABLE_WALL_WIDTH/2. If the PICTURE_WEIGHT is "light", recommend using a simple nail or adhesive hook; if  the PICTURE_WEIGHT is "medium", recommend a picture hook or wall anchor; the PICTURE_WEIGHT is "heavy", recommend hammering a nail into one of the vertical wooden studs behind the wallboard, adding guidance that American homes are usually built with studs placed every 16 inches on-center. If the WALL_TYPE is "reinforced", explain that you can hang any reasonably sized picture by hammering one or more nails into the plywood behind the wallboard. Also mention that you can place painter's tape on the wall where you plan to drill or hammer to prevent the wall from chipping and making dust. After typing out these instructions, write a prompt to be entered in ChatGPT to generate a diagram illustrating the measurements supplied by the user, eg EYE_HEIGHT, PICTURE_HEIGHT, DROP_TO_HARDWARE, and NAIL_HORIZONTAL_POSITION. Your prompt should ask ChatGPT to draw this in the style of an architectural blueprint with white lines and text on a dark blue background. Your prompt should clarify that the diagram should be as easy to follow as possible, with no extraneous text or imagery. Finally, type a message to the user suggesting she or he enter this prompt into ChatGPT.com to generate a useful diagram."""

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
                "help": "Are you measuring dimensions in inches or centimeters? (Whole numbers without fractions or decimals will suffice)",
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
