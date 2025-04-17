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
    "button_text": "Learn to make an AI MicroApp like this",
    "url": "https://www.youtube.com/watch?v=jqpEJ2995IA"    
}

SYSTEM_PROMPT = """Acting as an expert in curating displays of art in homes, galleries, and museums, you will generate concise instructions in plain language understandable by a lay person on how to hang a picture, specifically where to place a nail in accordance with the measurements of the wall and picture supplied in the prompt. Your calculations will depend on the following fields from the user:

EYE_HEIGHT: This will be the height off the floor of the eye level of a typical standing viewer.

PICTURE_HEIGHT: This will be the vertical dimension of the picture.
																DROP_TO_HARDWARE: This will be the distance between the top of the picture to the wire, cleat, or other hanging hardware attached to the back of the picture. In almost every case, the hardware will be screwed or adhered to the back of the picture so as to be invisible to the viewer; the viewer will not see the nail or wire sticking out above the picture frame.
																AVAILABLE_WALL_WIDTH: This is the running length of wall space available to mount the picture; it is bounded by obstacles to the left and right such as wall corners, furniture, or other hangings.

NAIL_HORIZONTAL_POSITION: This will be the distance from the left or right edge of the AVAILABLE_WALL_WIDTH to the placement of the nail. It is not the distance between the edge of the picture and the nail location.
"""

PHASES = {
   "dimension_calculations": {
        "name": "Calculate your nail's position",
        "fields": {
            "info": {
                "type": "markdown",
                "body": "Use a tape measure to find the following dimensions."
            },
            "measurement_units": {
                "type": "selectbox",
                "options": ['inches', 'centimeters'],
                "label": "Are you measuring dimensions in inches or centimeters?",
                "help": "Whole numbers without fractions or decimals will suffice",
            },
            "viewer_height_inches": {
                "type": "slider",
                "min_value": 60,
                "max_value": 75,
                "label": "How tall is your average viewer in inches? (The average American height is 66 in.)",
                "showIf": {"measurement_units": "inches"},
            },
            "viewer_height_centimeters": {
                "type": "slider",
                "min_value": 155,
                "max_value": 180,
                "label": "How tall is your average viewer in centimeters? (The average American height is 168 cm.)",
                "showIf": {"measurement_units": "centimeters"},
            },
            "picture_height": {
                "type": "number_input",
                "step": 1,
                "label": "What's the height of your picture, including the frame? (You can just type a whole number)",
            },
            "drop_to_hardware": {
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
            "picture_weight": {
                "type": "selectbox",
                "options": ['light (under 5 pounds)', 'medium (5-20 pounds)', 'heavy (over 20 pounds)'],
                "label": "How heavy is the picture?",
                "help": "Include the frame and glazing (glass or Plexi front}, if any"
            },
            "wall_type": {
                "type": "selectbox",
                "options": ['normal', 'reinforced'],
                "label": "What type of wall are you hanging on?",
                "help": "Most American rooms have normal drywall, but some galleries are reinforced with plywood backing"
            },
        },
        "user_prompt": [
            {
                "condition": {},
                "prompt": "Please use {measurement_units} in all of your output for this prompt."
            },
            {
                "condition": {},
                "prompt": """For future reference, note the following values entered by the user:
                PICTURE_HEIGHT: {picture_height}
																			DROP_TO_HARDWARE: {drop_to_hardware}
																			AVAILABLE_WALL_WIDTH: {available_wall_width}
                """
            },
            {
                "condition": {"measurement_units": "inches"},
                "prompt": "- Start off by calculating the EYE_HEIGHT = .93 * {viewer_height_inches}.\n",
            },
            {
                "condition": {"measurement_units": "centimeters"},
                "prompt": "- Start off by calculating the EYE_HEIGHT = .93 * {viewer_height_centimeters}.\n",
            },
            {
                "condition": {},
                "prompt": "- Calculate the nail's height off the floor using the formula NAIL_HEIGHT = EYE_HEIGHT + ({picture_height}/2) - {drop_to_hardware}."
            },
            {
                "condition": {},
                "prompt": "- Calculate the nail's distance from the nearest horizontal obstacle using the formula NAIL_HORIZONTAL_POSITION = {available_wall_width}/2. Explain how you arrived at these calculations."
            },
            {
                "condition": {},
                "prompt": "- Report the values you just calculated. What numbers did you get for NAIL_HEIGHT and NAIL_HORIZONTAL_POSITION in {measurement_units}?'\n",
            },
            {
                "condition": {"$and":[{"picture_weight": "light"},{"wall_type": "normal"}]},
                "prompt": "- Recommend a simple nail or adhesive hook.\n",
            },
            {
                "condition": {"$and":[{"picture_weight": "medium"},{"wall_type": "normal"}]},
                "prompt": "- Recommend a picture hook or wall anchor to compensate for the picture's weight.  Also mention that you can place painter's tape on the wall where you plan to drill or hammer to prevent the wall from chipping and making dust. \n",
            },
            {
                "condition": {"$and":[{"picture_weight": "heavy"},{"wall_type": "normal"}]},
                "prompt": "- Recommend hammering one or more nails into one of the vertical wooden studs behind the wallboard, adding guidance that American homes are usually built with studs placed every 16 inches on-center.\n",
            },
            {
                "condition": {"wall_type": "reinforced"},
                "prompt": "- Explain that you can hang any reasonably sized picture by hammering one or more nails into the plywood behind the wallboard.\n",
            },
            {
                "condition": {},
                "prompt": "- Now tell the user exactly where to place the nail, specifically the NAIL_HEIGHT and NAIL_HORIZONTAL_POSITION in {measurement_units}. Do not tell them how to do the calculations; just do the calculations yourself and tell the user the results. For example, instead of writing 'Hammer the nail NAIL_HEIGHT above the floor' fill in the word NAIL_HEIGHT with the specific number you calculated.'\n",
            },
            {
                "condition": {},
                "prompt": "- After typing out the preceding information, think of a prompt that can be entered in ChatGPT to generate a diagram illustrating the measurements supplied by the user. Your image prompt should label {eye_height} as the height of the picture, {drop_to_hardware} as the distance from the top of the picture down to the wire or other hanging hardware, and {nail_horizontal_position} as the distance between the nail and a nearby wall or obstacle. Your prompt should ask ChatGPT to draw this in the style of an architectural blueprint with white lines and text on a dark blue background. Your prompt should clarify that the diagram should be as easy to follow as possible, with no extraneous text or imagery. Finally, type a message to the user suggesting entering this prompt into ChatGPT.com to generate a useful diagram.\n",
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
