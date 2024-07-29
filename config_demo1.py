APP_TITLE = "MicroApp Demo App #1"
APP_INTRO = """This app demonstrates all the fields that are available to a micro-app. It can be used to understand what kinds of inputs a micro-app can ask for, and how to configure those fields. 
"""

APP_HOW_IT_WORKS = """
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You provide brief 1-2 sentence answers to the instructions you are provided. You never ask questions in your responses. """

PHASES = {
    "phase1": {
        "name": "Text Input",
        "fields": {
            "name": {
                "type": "text_input",
                "label": """What is your first name?""",
                "value": "John",
            }

        },
        "phase_instructions": "The user will provide their name. Please welcome them by name. ",
        "user_prompt": "{name}",
        "allow_skip": True,
    },
    "phase2": {
        "name": "Text Area",
        "fields": {
            "hobbies": {
                "type": "text_area",
                "height": 200,
                "label": """What are your favorite hobbies?""",
                "value": "Golf, Crossword Puzzles, Fantasy Football",
            }
        },
        "phase_instructions": "The user will introduce their hobbies now, and I'll say what I like about one of those hobbies. ",
        "user_prompt": "{hobbies}",
        "allow_skip": True,
  
    },
    "phase3": {
        "name": "Radio Select",
        "fields": {
            "pluto": {
                "type": "radio",
                "options": ['Yes!', 'No', 'It is whatever NASA tells me it is.'],
                "label": "Is Pluto a planet?",
            }
        },
        "phase_instructions": "The user has been asked 'Is pluto a planet?' and will give their response. Comment on their response",
        "user_prompt": "{pluto}",
        "allow_skip": True,
    },
    "phase4": {
        "name": "Dropdown Select",
        "fields": {
            "tech": {
                "type": "selectbox",
                "options": ['Mac', 'PC', 'Linux!', 'Stone Tablet'],
                "label": "Mac or PC?",
            }
        },
        "phase_instructions": "The user will tell you whether they prefer Mac, PC, Linux or provide a flippant answer about their choice of technology. Tell them a joke about whatever their choice is.",
        "user_prompt": "{tech}",
        "allow_skip": True,
    },
    "phase5": {
        "name": "Checkbox",
        "fields": {
            "check_me": {
                "type": "checkbox",
                "label": "Check this box!",
            }
        },
        "phase_instructions": "The user will tell you if they have pets or not. Comment on it.",
        "ai_response": False,
        "custom_response": "Thanks!",
        "allow_skip": True,
    },
    "phase6": {
        "name": "age",
        "fields": {
            "age": {
                "type": "slider",
                "min_value": 5,
                "max_value": 100,
                "label": "How old are you?",
            }
        },
        "phase_instructions": "The user will provide their age. Say something encouraging about their age.",
        "user_prompt": "{age}",
        "allow_skip": True,
    },
    "phase7": {
        "name": "mars",
        "fields": {
            "mars": {
                "type": "number_input",
                "step": 1,
                "label": "In what year do you think the first human will reach step foot on Mars?",
            }
        },
        "phase_instructions": "The user will predice what year the first person will step foot on Mars. React to their answer. If their answer is non-sensical, provide a sarcastic comment.",
        "user_prompt": "{mars}",
        "allow_skip": True,
    }

}

def prompt_conditionals(prompt, user_input, phase_name=None):
    #TO-DO: This is a hacky way to make prompts conditional that requires the user to know a lot of python and get the phase and field names exactly right. Future task to improve it. 




    return prompt
    
selected_llm = "gpt-4o-mini"


LLM_CONFIGURATIONS = {
    "gpt-4o-mini": {
        "model": "gpt-4o-mini",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.150,
        "price_output_token_1M":.600
    },
    "gpt-4-turbo": {
        "model": "gpt-4-turbo",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":10,
        "price_output_token_1M":30
    },
    "gpt-4o": {
        "model": "gpt-4o",
        "frequency_penalty": 0,
        "max_tokens": 250,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":5,
        "price_output_token_1M":15
    },
    "gemini-1.0-pro": {
        "model": "gemini-1.0-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.5,
        "price_output_token_1M":1.5
    },
    "gemini-1.5-flash": {
        "model": "gemini-1.5-flash",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.35,
        "price_output_token_1M":1.05
    },
    "gemini-1.5-pro": {
        "model": "gemini-1.5-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":3.5,
        "price_output_token_1M":10.50
    },
    "claude-3.5-sonnet": {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-opus": {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 15,
        "price_output_token_1M": 75
    },
    "claude-sonnet": {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-haiku": {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 0.25,
        "price_output_token_1M": 1.25
    }
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
