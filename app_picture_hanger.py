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

SYSTEM_PROMPT = """Acting as an expert in curating displays of art in homes, galleries, and museums, you will generate concise instructions in plain language understandable by a lay person on how to hang a picture, specifically where to place a nail in accordance with the measurements of the wall and picture supplied in the prompt."""

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
            "viewer-height-centimeters": {
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
            "available-wall-width": {
                "type": "number_input",
                "step": 1,
                "label": "How much horizontal wall space is available?",
                "help": "Include the total span in the units you chose (inches or cm), eg between adjacent walls, nearby furniture, or pictures to the left and right.",
            },
            "picture-weight": {
                "type": "selectbox",
                "options": ['light (under 5 pounds)', 'medium (5-20 pounds)', 'heavy (over 20 pounds)'],
                "label": "How heavy is the picture?",
                "help": "Include the frame and glazing (glass or plastic}, if any"
            },
            "wall-type": {
                "type": "selectbox",
                "options": ['normal', 'reinforced'],
                "label": "What type of wall are you hanging on?",
                "help": "Most American rooms have normal drywall, but some galleries are reinforced with plywood backing"
            },
        },
        "user_prompt": [
            {
                "condition": {},
                "prompt": "Please use \"{measurement-units}\" in all of your output for this prompt."
            },
            {
                "condition": {"measurement-units": "inches"},
                "prompt": "- Start off by calculating the EYE_HEIGHT = .93 * \"viewer-height-inches\".\n",
            },
            {
                "condition": {"measurement-units": "centimeters"},
                "prompt": "- Start off by calculating the EYE_HEIGHT = .93 * \"viewer-height-centimeters\".\n",
            },
            {
                "condition": {},
                "prompt": "- Calculate the nail's height off the floor using the formula NAIL_HEIGHT = EYE_HEIGHT + (\"{picture_height}\"/2) - \"{drop-to-hardware}\"."
            },
            {
                "condition": {},
                "prompt": "- Calculate the nail's distance from the nearest horizontal obstacle using the formula NAIL_HORIZONTAL_POSITION = \"{available-wall-width}\"/2."
            },
            {
                "condition": {"$and":[{"picture-weight": "light"},{"wall-type": "normal"}]},
                "prompt": "- Recommend a simple nail or adhesive hook.\n",
            },
            {
                "condition": {"$and":[{"picture-weight": "medium"},{"wall-type": "normal"}]},
                "prompt": "- Recommend a picture hook or wall anchor to compensate for the picture's weight.  Also mention that you can place painter's tape on the wall where you plan to drill or hammer to prevent the wall from chipping and making dust. \n",
            },
            {
                "condition": {"$and":[{"picture-weight": "heavy"},{"wall-type": "normal"}]},
                "prompt": "- Recommend hammering one or more nails into one of the vertical wooden studs behind the wallboard, adding guidance that American homes are usually built with studs placed every 16 inches on-center.\n",
            },
            {
                "condition": {"wall-type": "reinforced"},
                "prompt": "- Explain that you can hang any reasonably sized picture by hammering one or more nails into the plywood behind the wallboard.\n",
            },
            {
                "condition": {},
                "prompt": "- Now tell the user exactly where to place the nail, specifically the NAIL_HEIGHT and NAIL_HORIZONTAL_POSITION in \"{measurement-units}\".\n",
            },
            {
                "condition": {},
                "prompt": "- After typing out the preceding information, think of a prompt that can be entered in ChatGPT to generate a diagram illustrating the measurements supplied by the user, eg EYE_HEIGHT, PICTURE_HEIGHT, DROP_TO_HARDWARE, and NAIL_HORIZONTAL_POSITION. Your prompt should ask ChatGPT to draw this in the style of an architectural blueprint with white lines and text on a dark blue background. Your prompt should clarify that the diagram should be as easy to follow as possible, with no extraneous text or imagery. Finally, type a message to the user suggesting entering this prompt into ChatGPT.com to generate a useful diagram.\n",
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
