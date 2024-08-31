APP_TITLE = "Alt Text Generator"
APP_INTRO = """This app accepts images via upload or URL and returns alt text for accessibility."""

APP_HOW_IT_WORKS = """
This app creates alt text for accessibility from images. 
                For most images, it provides brief alt text to describe the image, focusing on the most important information first. 

                For complex images, like charts and graphs, the app creates a short description of the image and a longer detail that describes what the complex image is conveying. 

                For more information, see <a href="https://www.w3.org/WAI/tutorials/images/" target="_blank">W3C Images Accessibility Guidelines</a>
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You accept images in url and file format to generate description or alt text according to WCAG and ADA standards."""

PHASES = {
    "phase1": {
        "name": "Image Input and Alt Text Generation",
        "fields": {
            "http_img_urls": {
                "type": "text_area",
                "label": "Enter image urls"
            },
            "uploaded_files": {
                "type": "file_uploader",
                "label": "Choose files",
                "allowed_files": ['png', 'jpeg', 'gif', 'webp'],
                "multiple_files": True,
            },
            "important_text": {
                "type": "checkbox",
                "label": "The text in my image(s) is important",
                "value": False,
                "help": "If text is important, it should be included in the alt text. If it is irrelevant or covered in text elsewhere on the page, it should not be included"
            },
            "complex_image": {
                "type": "checkbox",
                "label": "My image is a complex image (chart, infographic, etc...)",
                "value": False,
                "help": "Complex images get both a short and a long description of the image"
            }
        },
        "phase_instructions": "Generate the alt text for the image urls and uploads",
        "user_prompt": [
            {
                "condition": {"important_text": False,"complex_image": False},
                "prompt": """I am sending you one or more images. Please provide separate appropriate alt text for each image I send. The alt text should:
                - Aim to put the most important information at the beginning."""
            },
            {
                "condition": {"complex_image": True},
                "prompt": """I am sending you one or more complex images. Please provide a short description to identify the image, and a long description to represent the essential information conveyed by the image. \n
                Please provide your output in this format \n
                **Short Description:**\n
                [Short Description]\n\n
                **Long Description:**\n
                [Long Description]\n"""
            },
            {
                "condition": {"important_text": True, "complex_image": False},
                "prompt": """I am sending you one or more images. Please provide separate appropriate alt text for each image I send. The alt text should:
                - Aim to put the most important information at the beginning. \n
                - Make sure to include any text in this image as part of the alt text"""
            },
            {
                "condition": {},
                "prompt": "Here is the uploaded image(s) - {http_img_urls} and uploaded_files",
            }
        ],
        "show_prompt": True,
        "allow_skip": False,
    }
}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Thanks for using the Alt Text Generator service"
COMPLETION_CELEBRATION = False