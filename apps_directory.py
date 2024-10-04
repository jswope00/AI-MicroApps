import os
import importlib
import streamlit as st

# Path to the current directory (where the apps are located)
CURRENT_DIR = os.path.dirname(__file__)
APP_IMAGES_DIR = os.path.join(CURRENT_DIR, "app_images")  # Folder where app images are stored


def get_app_metadata(app_file):
    """Dynamically import each app file and extract its metadata."""
    module_name = os.path.splitext(app_file)[0]
    app_module = importlib.import_module(module_name)

    # Use the provided APP_IMAGE from the app module, or fall back to a placeholder image
    image_file_name = getattr(app_module, "APP_IMAGE", "placeholder.png")  # Assume default image is 'placeholder.jpg'
    image_path = os.path.join(APP_IMAGES_DIR, image_file_name)

    # If the image doesn't exist, fall back to the placeholder image
    if not os.path.exists(image_path):
        image_path = os.path.join(APP_IMAGES_DIR, "placeholder.jpg")

    # Extract metadata from the app module
    metadata = {
        "title": getattr(app_module, "APP_TITLE", module_name.replace("app_", "").replace("_", " ").title()),
        "description": getattr(app_module, "APP_INTRO", "No description provided."),
        "image": image_path,
        "url": getattr(app_module, "APP_URL", app_file),
        "published": getattr(app_module, "PUBLISHED",False),
    }
    return metadata

# Function to display the apps
def display_apps(apps_metadata):
    """Display the apps in a 4x4 grid layout with clickable titles and tooltip for descriptions."""
    # Add some custom CSS for the tooltip effect
    st.markdown("""
        <style>
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
            font-size: 18px;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: #555;
            color: #fff;
            text-align: left;
            border-radius: 5px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        /* Align the elements to the right */
        .app-title-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .right-side-icons {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-left: auto;
        }
        </style>
    """, unsafe_allow_html=True)

    cols = st.columns(4)  # Create four columns for the grid layout
    app_number = 1  # Initialize a counter for numbering apps

    for idx, app in enumerate(apps_metadata):
        if app.get('published', False):  # Check if the app is published
            col = cols[(app_number-1) % 4]  # Cycle through the columns
            with col:
                with st.expander(f"MicroApp {app_number}", expanded=True):
                    st.image(app["image"], use_column_width=True)
                    st.markdown(f"""
                        <div class="app-title-container">
                            <strong>{app['title']}</strong>
                                <div class="right-side-icons">
                                    <div class="tooltip"> ℹ️
                                        <span class="tooltiptext" style="font-size:12px;">{app['description']}</span>
                                    </div>
                                    <a href="{app['url']}" target="_blank" style="text-decoration:none;">
                                        <span style="font-size:18px;">↗️</span>
                                    </a>
                                </div>
                        </div>
                        """, unsafe_allow_html=True)
            app_number += 1  # Increment the counter


def main():
    st.set_page_config(page_title="AI MicroApps", page_icon="🤖", layout="wide")
    st.title("AI MicroApps Directory")

    # Scan for all app files (starting with 'app_' and ending in '.py')
    apps_metadata = []
    for app_file in os.listdir(CURRENT_DIR):
        if app_file.startswith("app_") and app_file.endswith(".py"):
            metadata = get_app_metadata(app_file)
            apps_metadata.append(metadata)

    # Sort apps metadata alphabetically by title
    apps_metadata.sort(key=lambda x: x["title"])

    # Display apps in a 4x4 grid
    if apps_metadata:
        display_apps(apps_metadata)
    else:
        st.warning("No apps found.")

if __name__ == "__main__":
    main()
