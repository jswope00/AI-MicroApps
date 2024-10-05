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
        "published": getattr(app_module, "PUBLISHED", False),
    }
    return metadata

# Function to display the apps
def display_apps(apps_metadata):
    """Display the apps in a responsive card layout grid."""
    # Add custom CSS for card styling
    st.markdown("""
        <style>
        .card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            transition: 0.3s;
            margin-bottom: 20px;
            text-align: center;
        }
        .card:hover {
            box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.3);
        }
        .card img {
            border-radius: 10px;
            width: 100%;
            height: auto;
            object-fit: cover;
        }
        .card-title {
            font-size: 24px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 15px;
            color: #333;
        }
        .card-description {
            font-size: 16px;
            color: #666;
            margin-bottom: 15px;
            font-weight: normal;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 5; /* Limit to 5 lines */
            -webkit-box-orient: vertical;
        }
        .card a {
            text-decoration: none;
            color: #0066cc;
            font-weight: bold;
        }
        .card a:hover {
            text-decoration: underline;
        }
        a.no-underline,
        a.no-underline:hover {
            text-decoration: none;
        }
        </style>
    """, unsafe_allow_html=True)

    # Creating a responsive card layout
    cols = st.columns(4)  # Define a 4-column layout, adjust as necessary
    app_number = 1  # Initialize a counter for numbering apps

    for idx, app in enumerate(apps_metadata):
        if app.get('published', False):  # Check if the app is published
            col = cols[(app_number-1) % 4]  # Cycle through the columns
            with col:
                st.markdown(f"""
                    <a class="no-underline" href="{app['url']}" target="_blank"><div class="card">
                        <img src="data:image/jpeg;base64,{get_image_base64(app['image'])}" alt="{app['title']}">
                        <div class="card-title">{app['title']}</div>
                        <div class="card-description">{app['description']}</div>
                        <a href="{app['url']}" target="_blank">View App</a>
                    </div></a>
                """, unsafe_allow_html=True)
            app_number += 1  # Increment the counter

def get_image_base64(image_path):
    """Convert image to base64 for inline rendering."""
    import base64
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

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
