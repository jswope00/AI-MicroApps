APP_URL = "https://think-pair-share.streamlit.app"
APP_IMAGE = "think_pair_share.webp"
PUBLISHED = True

APP_TITLE = "Think-Pair-Share with an AI Partner"
APP_INTRO = """
In this interactive exercise, you will participate in a structured think-pair-share with an AI partner, offering you a chance to both critique an AI response and refine your own.
"""

APP_HOW_IT_WORKS = ""

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You provide your own reflection on a topic for a think-pair-share activity with a human partner. """

PHASES = {
    "phase1": {
        "name": "Individual Reflection",
        "fields": {
            "prompt": {
                "type": "markdown",
                "body": """<strong>Reflection Prompt:</strong>
                <p>Imagine you are a policy advisor tasked with proposing a solution to mitigate the environmental impact of large-scale AI systems. You have the budget to implement one of the following options:</p>
<ol>
                <li>Invest in green energy infrastructure to power data centers exclusively with renewable energy.</li>
                <li>Develop more energy-efficient algorithms and incentivize research into low-power AI models.</li>
                <li>Implement strict regulations limiting the number of computations or the size of models allowed in commercial AI applications.</li>
                </ol>""",
                "unsafe_allow_html": True, 
                
            },
            "reflection": {
                "type": "text_area",
                "label": "Please write your initial thoughts about the topic provided. Responses should be at least 50 words, relevant to the prompt, and reflect on at least one of the three options.",
                "height": 300,
                "value": "As a policy advisor, I'd prioritize investing in green energy infrastructure to power data centers with renewable energy. While all options address AI's environmental impact, transitioning to renewable energy tackles the root cause of emissions without stifling innovation or progress in AI development. Energy-efficient algorithms are essential but may not scale quickly enough, and strict regulations risk slowing advancements or creating barriers for smaller companies. By ensuring data centers run on clean energy, we create a sustainable foundation for AI growth while reducing reliance on fossil fuels. This solution aligns environmental responsibility with the potential of AI-driven progress."
            }
        },
        "ai_response": True,
        "phase_instructions": "The user is reflecting on of these three topics: 1. Invest in green energy infrastructure to power data centers exclusively with renewable energy; 2. Develop more energy-efficient algorithms and incentivize research into low-power AI models; 3. Implement strict regulations limiting the number of computations or the size of models allowed in commercial AI applications. Simply acknowledge the user's reflection and provide no other feedback at this point.",
        "user_prompt": "Here is my reflection: {reflection}. ",
        "allow_skip": False,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
                1. Length
                    2 points - The user has provided a reflection that is at least 50 words.
                    0 points - The user has provided a reflection that is less than 50 words.
                2. Relevance
                    2 points - The user has provided a reflection that is relevant to the prompt.
                    0 points - The user has provided a reflection that is not relevant to the prompt.
                3. Options
                    2 points - The user has provided a reflection that reflects on at least one of the three options.
                    0 points - The user has provided a reflection that does not reflect on any of the three options.""",
    },
    "phase2": {
        "name": "AI Reflection",
        "fields": {
            "prompt": {
                "type": "markdown",
                "body": "Next, the AI will reflect on the same prompt you just responded to. You will have a chance to analyze and critique the AI reflection, or revise your own response based on the AI's reflection.",
                "unsafe_allow_html": True
            },
        },
        "ai_response": True,
        "button_label": "Proceed",
        "user_prompt": """Reflect on the following prompt. Reflections should be at least 50 words, relevant to the prompt, and reflect on a different option than the student has chosen: <strong>Reflection Prompt:</strong>
                <p>Imagine you are a policy advisor tasked with proposing a solution to mitigate the environmental impact of large-scale AI systems. You have the budget to implement one of the following options:</p>
<ol>
                <li>Invest in green energy infrastructure to power data centers exclusively with renewable energy.</li>
                <li>Develop more energy-efficient algorithms and incentivize research into low-power AI models.</li>
                <li>Implement strict regulations limiting the number of computations or the size of models allowed in commercial AI applications.</li>
                </ol>""",
    },
    "phase3": {
        "name": "Final Reflection and Sharing",
        "fields": {
            "critique": {
                "type": "text_area",
                "label": "After reviewing the AI's response, do you have any points of critique or analysis that you think could improve the AI's response?",
                "height": 200,
            },
            "reflection_v2": {
                "type": "text_area",
                "label": "After reviewing the AI's response and critique, you may revise your own reflection.",
                "height": 200,
            },
        },
        "ai_response": True,
        "user_prompt": "Here is my feedback on your reflection: {critique}. Very briefly respond to my feedback. Then, here is my second reflection: {reflection_v2}. If I have revised my original reflection, please respond to the revisions I've made. If not, simple acknowledge that I have not revised my reflection.",
    }
}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! You may simply finish here, or share your reflections with the class."
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Think-Pair-Share",
    "page_icon": "🤔",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())