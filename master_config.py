import os
import ast

# 1. Page Config - Dict
# PAGE_CONFIG = {
#     "page_title": "AI MicroApps", # title of app if one app is implemented
#     "page_icon": "🤖", # replace based on App if it is single
#     "layout": "centered",  # "centered" or "wide"
#     "initial_sidebar_state": "expanded"  # Options: "auto", "expanded", "collapsed"
# }

APP_TITLE = "AI Microapps" # fallback page title
PAGE_ICON = "🤖" # fallback favicon
LAYOUT = "centered" # "centered" or "wide"
INITIAL_SIDEBAR_STATE: "expanded" # Options: "auto", "expanded", "collapsed"

# 2. Sidebar State - Hidden, Collapsed, or Expanded
SIDEBAR_HIDDEN = False  # Set to True to completely hide the sidebar

def extract_app_title(file_path):
    """Extracts the value of 'APP_TITLE' from the given Python file."""
    with open(file_path, 'r') as file:
        file_content = file.read()
        try:
            parsed_content = ast.parse(file_content)
            for node in ast.walk(parsed_content):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == "APP_TITLE":
                            if isinstance(node.value, ast.Str):  # Handles string assignments
                                return node.value.s
        except SyntaxError:
            print(f"Syntax error in file: {file_path}")
    return None

def generate_config_dict(folder_path):
    """Generates a dictionary with APP_TITLE as the key and the filename (without .py extension) as the value."""
    config_dict = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            app_title = extract_app_title(file_path)
            if app_title:
                config_dict[app_title] = filename[:-3]  # Remove .py extension for the value
            else:
                print(f"APP_TITLE not found in file: {filename}")
    
    return config_dict

folder_path = 'config_files'  # Path to your folder
config_dict = generate_config_dict(folder_path)

TEMPLATES = config_dict
