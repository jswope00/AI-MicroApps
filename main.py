import openai
import os
from dotenv import load_dotenv
import re
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.let_it_rain import rain
from config import *

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

function_map = {
    "text_input": st.text_input,
    "text_area": st.text_area,
    "warning": st.warning,
    "button": st.button,
    "radio": st.radio,
    "markdown": st.markdown,
    "selectbox": st.selectbox
}

user_input = {}

def build_field(phase_name, fields):
    for field_key, field in fields.items():
        field_type = field.get("type", "")
        field_label = field.get("label", "")
        field_body = field.get("body", "")
        field_value = field.get("value", "")
        field_max_chars = field.get("max_chars", None)
        field_help = field.get("help", "")
        field_on_click = field.get("on_click", None)
        field_options = field.get("options", [])
        field_horizontal = field.get("horizontal", False)
        field_height = field.get("height", None)
        field_unsafe_html = field.get("unsafe_allow_html", False)
        field_placeholder = field.get("placeholder", "")

        kwargs = {}
        if field_label:
            kwargs['label'] = field_label
        if field_body:
            kwargs['body'] = field_body
        if field_value:
            kwargs['value'] = field_value
        if field_options:
            kwargs['options'] = field_options
        if field_max_chars:
            kwargs['max_chars'] = field_max_chars
        if field_help:
            kwargs['help'] = field_help
        if field_on_click:
            kwargs['on_click'] = field_on_click
        if field_horizontal:
            kwargs['horizontal'] = field_horizontal
        if field_height:
            kwargs['height'] = field_height
        if field_unsafe_html:
            kwargs['unsafe_allow_html'] = field_unsafe_html
        if field_placeholder:
            kwargs['placeholder'] = field_placeholder

        key = f"{phase_name}_phase_status"

        # If the user has already answered this question:
        if key in st.session_state and st.session_state[key]:
            # Write their answer
            if f"{phase_name}_user_input_{field_key}" in st.session_state:
                if field_type != "selectbox":
                    kwargs['value'] = st.session_state[f"{phase_name}_user_input_{field_key}"]
                kwargs['disabled'] = True

        my_input_function = function_map[field_type]

        with stylable_container(
                key="large_label",
                css_styles="""
                label p {
                    font-weight: bold;
                    font-size: 16px;
                }
                """,
        ):
            user_input[field_key] = my_input_function(**kwargs)

def call_openai_completions(system_message, user_message, scoring_instructions):
    full_system_message = f"{system_message}\n\n{scoring_instructions}"
    openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    llm_configuration = LLM_CONFIGURATION["gpt-4o"]
    response = openai_client.chat.completions.create(
        model=llm_configuration["model"],
        messages=[
            {"role": "system", "content": full_system_message},
            {"role": "user", "content": user_message}
        ],
        max_tokens=llm_configuration.get("max_tokens", 1000),
        temperature=llm_configuration.get("temperature", 1),
        top_p=llm_configuration.get("top_p", 1),
        frequency_penalty=llm_configuration.get("frequency_penalty", 0),
        presence_penalty=llm_configuration.get("presence_penalty", 0)
    )
    return response.choices[0].message.content

def st_store(input, phase_name, field_key, phase_key):
    key = f"{phase_name}_{field_key}_{phase_key}"
    st.session_state[key] = input


def build_scoring_instructions(rubric):
    scoring_instructions = f"""
    Please score the user's previous response based on the following rubric: \n{rubric}
    \n\nPlease output your response as JSON, using this format: {{ "[criteria 1]": "[score 1]", "[criteria 2]": "[score 2]", "total": "[total score]" }}
    """
    return scoring_instructions


def extract_score(text):
    pattern = r'"total":\s*"?(\d+)"?'
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        return 0


def check_scores(PHASE_NAME):
    phase_fields = PHASES[PHASE_NAME]["fields"]
    all_passed = True
    for field_key, field in phase_fields.items():
        if field.get("scored_phase", False):
            minimum_score = field.get("minimum_score", 1)  # Default minimum score is set to 1
            score_key = f"{PHASE_NAME}_{field_key}_ai_score"
            score = st.session_state.get(score_key, 0)
            if score < minimum_score:
                all_passed = False
    st.session_state[f"{PHASE_NAME}_phase_status"] = all_passed
    return all_passed


def skip_phase(PHASE_NAME, No_Submit=False):
    phase_fields = PHASES[PHASE_NAME]["fields"]
    for field_key in phase_fields:
        st_store(user_input, PHASE_NAME, field_key, "user_input")
        if No_Submit == False:
            st.session_state[f"{PHASE_NAME}_{field_key}_ai_response"] = "This phase was skipped."
    st.session_state[f"{PHASE_NAME}_phase_status"] = True
    st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)


def celebration():
    rain(
        emoji="🥳",
        font_size=54,
        falling_speed=5,
        animation_length=1,
    )

def display_results():
    st.header("Results")
    for phase_name, phase_results in st.session_state.get('results', {}).items():
        st.subheader(f"Results for {phase_name}")
        for result in phase_results:
            st.markdown(result)

def main():
    if 'CURRENT_PHASE' not in st.session_state:
        st.session_state['CURRENT_PHASE'] = 0
    if 'results' not in st.session_state:
        st.session_state['results'] = {}

    st.title(APP_TITLE)
    st.markdown(APP_INTRO)

    if APP_HOW_IT_WORKS:
        with st.expander("Learn how this works", expanded=False):
            st.markdown(APP_HOW_IT_WORKS)

    if SHARED_ASSET:
        with open(SHARED_ASSET["path"], "rb") as asset_file:
            st.download_button(label=SHARED_ASSET["button_text"],
                               data=asset_file,
                               file_name=SHARED_ASSET["name"],
                               mime="application/octet-stream")

    if HTML_BUTTON:
        st.link_button(label=HTML_BUTTON["button_text"], url=HTML_BUTTON["url"])

    i = 0

    while i <= st.session_state['CURRENT_PHASE']:
        submit_button = False
        next_phase_button = False
        skip_button = False
        final_phase_name = list(PHASES.keys())[-1]
        final_key = f"{final_phase_name}_ai_response"

        PHASE_NAME = list(PHASES.keys())[i]
        PHASE_DICT = PHASES[PHASE_NAME]
        fields = PHASE_DICT["fields"]

        st.write(f"#### Phase {i + 1}: {PHASE_DICT['name']}")

        build_field(PHASE_NAME, fields)

        key = f"{PHASE_NAME}_phase_status"

        markdown_phase = any(field["type"] == "markdown" for field in fields.values())

        if markdown_phase:
            if key not in st.session_state:
                st.session_state[key] = True
                st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)

        if key not in st.session_state:
            st.session_state[key] = False
        if st.session_state[key] != True and final_key not in st.session_state:
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    submit_button = st.button(label=PHASE_DICT.get("button_label", "Submit"), type="primary",
                                              key="submit " + str(i))
                with col2:
                    next_phase_button = st.button(label="Go to Next Phase", key="next_phase " + str(i))
                with col3:
                    if PHASE_DICT.get("allow_skip", False):
                        skip_button = st.button(label="Skip Question", key="skip " + str(i))

        for field_key in fields:
            if f"{PHASE_NAME}_user_input_{field_key}" in st.session_state:
                key = f"{PHASE_NAME}_{field_key}_ai_response"
                if key in st.session_state:
                    st.info(st.session_state[key], icon="🤖")
                key = f"{PHASE_NAME}_{field_key}_ai_result"
                if key in st.session_state and SCORING_DEBUG_MODE == True:
                    st.info(st.session_state[key], icon="🤖")

        if submit_button:
            for field_key, field in fields.items():
                st_store(user_input[field_key], PHASE_NAME, field_key, "user_input")
                user_response = user_input[field_key]
                system_instructions = PHASE_DICT.get("system_instructions", "")
                rubric = field.get("rubric", "")

                if field.get("scored_phase", False):
                    scoring_instructions = build_scoring_instructions(rubric)
                    evaluation = call_openai_completions(system_instructions, user_response, scoring_instructions)
                    st_store(evaluation, PHASE_NAME, field_key, "ai_response")
                    score = extract_score(evaluation)
                    st_store(score, PHASE_NAME, field_key, "ai_score")
                    feedback_message = f"""
                                        **Your Response:** {user_response}\n
                                        **AI Feedback:** {evaluation}\n
                                        **Score:** {score}
                                        """
                    st.markdown(feedback_message)
                    # Store feedback message in session state for later display
                    if PHASE_NAME not in st.session_state['results']:
                        st.session_state['results'][PHASE_NAME] = []
                    st.session_state['results'][PHASE_NAME].append(feedback_message)
                else:
                    feedback_message = f"""
                                        **Your Response:** {user_response}\n
                                        """
                    st.markdown(feedback_message)

                    # Store feedback message in session state for later display
                    if PHASE_NAME not in st.session_state['results']:
                        st.session_state['results'][PHASE_NAME] = []
                    st.session_state['results'][PHASE_NAME].append(feedback_message)



        if next_phase_button:
            if check_scores(PHASE_NAME):
                st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)
                st.rerun()
            else:
                st.warning("You haven't passed. Please try again.")

        if skip_button:
            skip_phase(PHASE_NAME)
            st.rerun()

        if final_key in st.session_state and i == st.session_state['CURRENT_PHASE']:
            st.success(COMPLETION_MESSAGE)
            if COMPLETION_CELEBRATION:
                celebration()

        i = min(i + 1, len(PHASES))

if __name__ == "__main__":
    main()
