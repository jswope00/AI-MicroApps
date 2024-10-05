<h1 align="center">AI MicroApps Template</h1>

<p align="center">
  <a href="https://ai-microapps.streamlit.app">Gallery</a> &bull; <a href="https://docs.ai-microapps.io">Documentation</a> &bull; <a href="https://www.youtube.com/@johnswope8421">YouTube</a>
</p>

<p align="center">
  AI Microapps are the simplest free way to build AI-powered web apps that you can personalize and share. 
</p>

<p>Let's explain with an ✨AI-powered✨ Haiku App</p>

<p>First, we configure about 10 lines to configure the app. Some lines configure two text fields to gather the users name and a favorite activity. The last line is the AI prompt that we'll send to AI with the user's input. It looks like this</p>


<p>Here is the app we get:</p>


<p>So what next?</p>
<p>Once you've mastered the basics, you can start building customized apps for those long, complicated prompts that you always have trouble remembering exactly how you did them. <i>And</i> you can share your apps with others, allowing them to quickly and intuitively use an AI chain that you've developed. </p>
<p>AI Microapps was built by an educator for the education sector. It works well as either:</p>
   <ul>
      <li><strong>A course accelerator</strong> - Build and share your customized <a href="https://mcq-wizard.streamlit.app" target="_blank" alt="Multiple Choice Question Generator">Multiple Choice Question generators</a>, Lesson Plan Builders, <a href="https://alt-text.streamlit.app" target="_blank">Alt Text Wizards</a> and more. </li>
      <li><strong>Assessment &amp; Feedback Tools</strong> - You can create AI-powered exercises for your students like an <a href="https://ai-debate.streamlit.app" target="_blank">AI Debate</a> tool about this week's lesson, or a <a href="https://critical-thinking.streamlit.app" target="_blank">critical thinking practice app</a> that is guided by your instruction. </li>
   </ul>
<p>AI MicroApps have nearly limitless customization capabilities and work with the most popular AI models, so you can make nearly any app and share it with anyone</p>

<p>Apps can be deployed to the web via <a href="https://streamlit.io/" target="_blank" alt="Streamlit Hosting">Streamlit</a> for free and nearly instantly.</p>

<p>Happy Building!</p>



## Demo

https://ai-microapps.streamlit.app

## Installation Video

https://www.youtube.com/watch?v=IXWzvWsavHs

## Overview

This Python application provides a template for creating AI-powered education apps like question generators, debate exercises, critical thinking assessments, and more. Apps can be configured by modifying python configuration files, without needing to touch or understand the core code. And multiple apps can be created by creating multiple configuration files. Apps are built to be customized for your specific use case and shared with others. 

Apps can be deployed for free via [Streamlit.io](https://streamlit.io). Please see Streamlit's instructions for deploying a web app from a git repository

## Structure
Microapps are built by combining **fields** and **phases**. **Fields** capture user input (e.g. responding to a faculty question, indicating a preference). **Phases** process fields, send a request to the AI, and receive a response. Phases can also be scored. 
<img width="632" alt="image" src="https://github.com/user-attachments/assets/69ce2508-7e56-4618-868f-e6e67dd2e449">

Explore the config_files/config_demo1.py file to see the supported fields and sample configuration. 
Explore the config_files/config_demo2.py file to see the supported phases and sample configuration. 

## Requirements

- Python 3.8+
- Streamlit
- AI API Keys (currently, OpenAI, Claude, and Gemini are supported. Want to request other? Submit an issue.)

## Installation

1. Fork the repository
   
2. Clone your new forked repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your OpenAI API key:
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:
     ```env
     OPENAI_API_KEY="your_openai_api_key"
     ```
   - Optionally, add Gemini and Claude keys
     ```env
     GOOGLE_API_KEY="your_google_api_key"
     CLAUDE_API_KEY="your_claude_api_key"
     ```

## Running the Application

To run the Streamlit application, execute the following command:
```bash
streamlit run main.py
```

## Configuration

Copy and rename a config file that serves as a good starting point for your app. 

Modify the configuration fields, and replace the existing phases and fields with your own. 

Edit master_config.py to add your config file to the `templates` JSON list in the following format: "Human Readable Name": "config_file_name". Note no `.py` at the end of the config file name. 

Any changes to a config file require a restart of Streamlit
   - Ctrl + C to quit Streamlit from your terminal
   - To start Streamlit again:

```bash
streamlit run main.py
``` 


## Deploy to the web
Follow [Streamlit's instructions](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app) to deploy your github URL to a free web address hosted by Streamlit. You will need to add your API key(s) to the Streamlit's Secrets area. 
