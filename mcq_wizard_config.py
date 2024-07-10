APP_TITLE = "MCQ Generator"
APP_INTRO = """This micro-app allows you to generate multiple-choice questions quickly and consistently. 

It work with either GPT-3.5 Turbo, GPT-4, or both.

Optionally, users can modify the AI configuration by opening the left sidebar.
"""

APP_HOW_IT_WORKS = """
 This is an **MCQ Generator** that can create multiple choice questions in different formats and for different subject domains depending on the user's input.

Using AI to provide feedback and score like this is a very experimental process. Some things to note: 

 - AIs make mistakes. Users are encourage to skip a question if the AI is not understanding them or giving good feedback. 
 - The AI might say things that it can't do, like "Ask me anything about the article". I presume further refinement can reduce these kinds of responses. 
 - Scoring is highly experimental. At this point, it should mainly be used to gauge if a user gave an approximately close answer to what the rubric suggests. It is not recommended to show the user the numeric score. 
 - Initial testing indicates that the AI is a very easy grader. This is probably good in this experiment, and it may be refined with different prompting. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = "You write pedagogically sound Multiple Choice Questions precisely according to user inputs."

PHASES = {
    "phase1": {
        "name": "Configure Questions",
        "fields": {
            "topic_content": {
                "type": "text_area",
                "label": "Enter the content for question generation:",
                "max_chars": 50000,
                "height": 200,
            },
            "original_content_only": {
                "type": "checkbox",
                "label": "Focus only on the provided text",
            },
            "learning_objective": {
                "type": "text_area",
                "label": "Specify a learning objective (optional):",
                "max_chars": 1000
            },
            "questions_num": {
                "label": "Number of questions:",
                "type": "selectbox",
                "options": [1, 2, 3, 4, 5],
            },
            "correct_ans_num": {
                "label": "Correct answers per question:",
                "type": "selectbox",
                "index": 0,
                "options": [1, 2, 3, 4],
            },
            "question_level": {
                "label": "Question difficulty level:",
                "type": "selectbox",
                "options": ['Grade School', 'High School', 'University', 'Other'],
                "index": 2,
            },
            "distractors_num": {
                "label": "Number of distractors:",
                "type": "selectbox",
                "options": [1, 2, 3, 4, 5],
                "index": 2,
            },
            "distractors_difficulty": {
                "label": "Distractors difficulty",
                "type": "selectbox",
                "options": ['Normal', 'Obvious', 'Challenging'],
                "index": 0,
            },
            "learner_feedback": {
                "type": "checkbox",
                "label": "Include Learner Feedback?",
            },
            "hints": {
                "type": "checkbox",
                "label": "Include hints?",
            },
            "output_format": {
                "label": "Output Format:",
                "type": "selectbox",
                "options": ['Plain Text', 'OLX']
            },

        },
        "phase_instructions": "At the end of your response, always tell me what AI model you are running.",
        "user_prompt": "Please write {questions_num} {question_level} level multiple-choice question(s), each with {correct_ans_num} correct answer(s) and {distractors_num} distractors, based on text that I will provide.\n\n",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 0,
        "rubric": """
            1. Questions
                1 points - The user generates any questions
                0 points - The user does not generate any questions
        """,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "phase2": {
        "name": "Configure Questions",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "What is your name?",
                "value": "John"
            }
        },
        "phase_instructions": "Respond in Spanish.",
        "user_prompt": "Say hello to me. My name is {name}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 0,
        "rubric": """
            1. Name
                1 points - The user gives you their name
                0 points - The user does not give you their name. 
        """,
        "allow_revisions": True,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": True,
        "read_only_prompt": False
    }

}

def prompt_conditionals(prompt, user_input, phase_name=None):
    #TO-DO: This is a hacky way to make prompts conditional that requires the user to know a lot of python and get the phase and field names exactly right. Future task to improve it. 

    if phase_name == "phase1":
        if user_input["original_content_only"] == True:
            prompt += "Please create questions based solely on the provided text. \n\n"
        else: 
            prompt += "Please create questions that incorporate both the provided text as well as your knowledge of the topic. \n\n"

        if user_input["distractors_difficulty"] == "Obvious":
            prompt += "Distractors should be obviously incorrect options. \n\n"
        elif user_input["distractors_difficulty"] == "Challenging":
            prompt += "Distractors should sound like they could be plausible, but are ultimately incorrect. \n\n"

        if user_input["learning_objective"]:
            prompt += "Focus on meeting the following learning objective(s) : {learning_objective} \n\n"

        if user_input["learner_feedback"]:
            prompt += "Please provide a feedback section for each question that says why the correct answer is the best answer and the other options are incorrect. \n\n"

        if user_input["hints"]:
            prompt += "Also, include a hint for each question.\n\n"

        if user_input["output_format"] == "OLX":
            prompt += "Please write your MCQs in Open edX OLX format\n\n"

        prompt += """
            Format each question like the following:
            Question: [Question Text] \n
            A) [Answer A] \n
            B) [Answer B] \n
            ....
            N) [Answer N] \n

            Solution: [Answer A, B...N]\n\n
            """

        if user_input["learner_feedback"]:
            prompt += "Feedback: [Feedback]\n\n"

        if user_input["hints"]:
            prompt += "Hint: [Hint]\n\n"

        prompt += "Here is the text: \n===============\n{topic_content}"


    return prompt
    
selected_llm = "gpt-3.5-turbo"


LLM_CONFIGURATIONS = {
    "gpt-3.5-turbo": {
        "model": "gpt-3.5-turbo-0125",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.50,
        "price_output_token_1M":1.50
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

COMPLETION_MESSAGE = ""
COMPLETION_CELEBRATION = False