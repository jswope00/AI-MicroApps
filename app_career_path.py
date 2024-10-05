APP_URL = "https://ai-career-path.streamlit.app"

PUBLISHED = False

APP_TITLE = "Career Path Recommendation"

APP_INTRO = """This app helps you find the best career path based on your preferences, experience, and qualifications."""

APP_HOW_IT_WORKS = """
This app collects information about your interests, experience, and qualifications. It uses a combination of logical conditions and AI to recommend a career path that suits you best.
"""

SHARED_ASSET = {}

HTML_BUTTON = {}

SYSTEM_PROMPT = """You are a career advisor. Based on a person's preferences, experience, and qualifications, you can recommend the most suitable career path."""

PHASES = {
    "phase1": {
        "name": "Personal Information",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "What is your first name?",
                "helper": "First name only, please",
                "value": "Jane"
            },
            "age": {
                "type": "number_input",
                "label": "What is your age?",
                "min_value": 16,
                "max_value": 65,
                "value": 25
            },
            "education_level": {
                "type": "radio",
                "label": "What is your highest level of education?",
                "options": ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "PhD"],
                "value": ""
            },
            "experience_years": {
                "type": "number_input",
                "label": "How many years of work experience do you have?",
                "min_value": 0,
                "max_value": 40,
                "value": 0
            },
            "current_field": {
                "type": "text_input",
                "label": "What is your current field of work? (If applicable)",
                "value": "",
                "showIf": {"experience_years": {"$gt": 0}}
            }
        },
        "phase_instructions": "Please provide your basic details.",
        "user_prompt": [
            {
                "condition": {"$and": [{"age": {"$lt": 25}}, {"education_level": "Bachelor's Degree"}]},
                "prompt": "I am {name}, aged {age}. I recently completed my Bachelor's Degree and have {experience_years} years of experience in {current_field}. I'm eager to explore my career options."
            },
            {
                "condition": {"$and": [{"age": {"$gte": 25}}, {"experience_years": {"$gte": 5}}]},
                "prompt": "My name is {name}, and I am {age} years old. With a {education_level} and over {experience_years} years of experience in {current_field}, I'm seeking to advance my career to the next level."
            },
            {
                "condition": {"experience_years": {"$lt": 2}},
                "prompt": "I am {name}, {age} years old, with an education level of {education_level} and less than {experience_years} years of experience in {current_field}. I'm looking to enter a field where I can grow and gain more experience."
            }
        ],
        "show_prompt": True,
        "allow_skip": True
    },
    "phase2": {
        "name": "Career Preferences",
        "fields": {
            "preferred_working_style": {
                "type": "radio",
                "label": "What is your preferred working style?",
                "options": ["Team-oriented", "Independent"]
            },
            "technical_or_non_technical": {
                "type": "radio",
                "label": "Do you prefer a technical or non-technical role?",
                "options": ["Technical", "Non-technical"]
            },
            "willing_to_relocate": {
                "type": "radio",
                "label": "Are you willing to relocate?",
                "options": ["Yes", "No"],
            },
            "desired_salary": {
                "type": "number_input",
                "label": "What is your desired salary? (in $K)",
                "min_value": 30,
                "max_value": 300,
                "value": 60
            }
        },
        "phase_instructions": "Let us know more about your career preferences.",
        "user_prompt": [
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Independent"},
                    {"technical_or_non_technical": "Technical"}
                ]},
                "prompt": "I prefer working independently and I am interested in a technical role. I have {experience_years} years of experience in {current_field}, and I am looking for a career that suits my skills and preferences."
            },
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Independent"},
                    {"technical_or_non_technical": "Non-technical"}
                ]},
                "prompt": "I prefer working independently in a non-technical role. I have {experience_years} years of experience in {current_field}, and I am looking for a career that allows me to leverage my skills in a flexible work environment."
            },
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Team-oriented"},
                    {"technical_or_non_technical": "Technical"}
                ]},
                "prompt": "I enjoy working in a team and am interested in a technical role. I have {experience_years} years of experience in {current_field}, and I am looking for a collaborative environment where I can contribute my technical skills."
            },
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Team-oriented"},
                    {"technical_or_non_technical": "Non-technical"}
                ]},
                "prompt": "I enjoy working in a team and prefer non-technical roles. I have {experience_years} years of experience in {current_field}, and I am looking for a career that aligns with my interests and abilities."
            },
            {
                "condition": {"$and": [
                    {"willing_to_relocate": "Yes"},
                    {"desired_salary": {"$gt": 100}}
                ]},
                "prompt": "I am open to relocating for a job opportunity, and I am aiming for a salary above $100K. Please suggest a career path that fits these preferences."
            }
        ],
        "show_prompt": True,
        "allow_skip": True
    }
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = False
DISPLAY_COST = True

COMPLETION_MESSAGE = "Thank you for using the Career Path Recommendation app! We hope our suggestions help guide your professional journey."
COMPLETION_CELEBRATION = True

RAG_IMPLEMENTATION = True
SOURCE_DOCUMENT = "sample.pdf"

PAGE_CONFIG = {
    "page_title": "Career Advisor",
    "page_icon": "️🎓",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())