APP_TITLE = "My First App"
APP_INTRO = """This is a template for an AI-powered Microapp that transforms complex AI prompts into intuitive, user-friendly and _shareable_ applications. The application works like a form that anyone can fill out to get consistent results. 
"""

APP_HOW_IT_WORKS = """
AI-Powered Microapps work by simplifying the creation of consistent and customized outputs from complex AI prompts. Here’s how they operate:

**1. Define the Inputs:** Begin by selecting the important user-defined variables within your AI prompt. These become the input fields in your microapp.

**2. Construct the Prompt(s):** Define the prompts with placeholders for the inputs that will come from the form. Additional internal prompts can be added, for example for scoring. Finally, prompts can be conditional so they are only sent if certain conditions are met. 

**3. User completes the form:** The microapp presents these fields as a form, and the prompt(s) is/are dynamically generated as the form is filled out. This form is designed for ease of use, allowing anyone to input the necessary details without needing to remember or interact with the AI’s underlying complexities.

**4. Deliver Consistent Results:** Once the form is completed, the microapp generates the AI’s response based on the assembled prompt. This process ensures consistent and reliable outputs, regardless of who uses the microapp. The results can then be used directly, shared, or further customized as needed.

**Benefits:**

- Ease of Use: AI-Powered Microapps make advanced AI accessible by converting complex prompts into simple forms.
- Customization: Each microapp is built to suit your specific requirements, ensuring personalized AI interactions.
- Shareability: Microapps can be easily shared across teams, organizations, or communities, providing everyone with consistent, high-quality AI outputs.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = ""

PHASES = {}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "My First App",
    "page_icon": "🌐",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

TEMPLATES = {"My First App":"my_first_app"}

from main import main
if __name__ == "__main__":
    config = {
        "APP_TITLE": APP_TITLE,
        "APP_INTRO": APP_INTRO,
        "APP_HOW_IT_WORKS": APP_HOW_IT_WORKS,
        "HTML_BUTTON": HTML_BUTTON,
        "PREFERRED_LLM": PREFERRED_LLM,
        "LLM_CONFIG_OVERRIDE": LLM_CONFIG_OVERRIDE,
        "PHASES": PHASES,
        "COMPLETION_MESSAGE": COMPLETION_MESSAGE,
        "COMPLETION_CELEBRATION": COMPLETION_CELEBRATION,
        "SCORING_DEBUG_MODE": SCORING_DEBUG_MODE,
        "DISPLAY_COST": DISPLAY_COST,
        "RAG_IMPLEMENTATION": RAG_IMPLEMENTATION,
        "SOURCE_DOCUMENT": SOURCE_DOCUMENT,
        "PAGE_CONFIG": PAGE_CONFIG,
        "SIDEBAR_HIDDEN": SIDEBAR_HIDDEN,
        "TEMPLATES": TEMPLATES
    }
    main(config)