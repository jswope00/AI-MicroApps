# AI-Microapp-Template-Completion-v2

## Overview

This Streamlit application provides a guided critical analysis exercise for students to evaluate a research paper. The exercise is divided into multiple phases, with each phase containing specific questions. The application utilizes OpenAI's GPT model to provide feedback and scores based on a predefined rubric.

## Features

- **Step-by-Step Guidance:** Students are guided through different phases to analyze a research paper.
- **Automated Feedback and Scoring:** Utilizes OpenAI's GPT model to provide feedback and scores based on a faculty-defined rubric.
- **Interactive UI:** Students can see their progress, responses, AI feedback, and scores for each phase.
- **Persistent Results Display:** All feedback and scores are displayed persistently on the screen for review.

## Requirements

- Python 3.8+
- Streamlit
- OpenAI API Key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

## Configuration

Update the `config.py` file with the necessary configuration details, including the phases and rubrics for the exercise.

## Running the Application

To run the Streamlit application, execute the following command:
```bash
streamlit run main.py
```

## Usage

1. Open the provided URL in your browser.
2. Follow the step-by-step instructions to complete the critical analysis exercise.
3. Submit your responses for each phase to receive feedback and scores.
4. Review the feedback and scores displayed on the screen.

## Customization

- **Phases and Rubrics:** Modify the `config.py` file to update the phases, questions, and rubrics according to your requirements.
- **Model Configuration:** Update the `LLM_CONFIGURATION` dictionary in `main.py` to change the model settings.
