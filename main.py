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
        field_value = field.get("value", "")
        field_max_chars = field.get("max_chars", None)
        field_help = field.get("help", "")
        field_placeholder = field.get("placeholder", "")

        kwargs = {}
        if field_label:
            kwargs['label'] = field_label
        if field_value:
            kwargs['value'] = field_value
        if field_max_chars:
            kwargs['max_chars'] = field_max_chars
        if field_help:
            kwargs['help'] = field_help
        if field_placeholder:
            kwargs['placeholder'] = field_placeholder

        key = f"{phase_name}_phase_status"

        if key in st.session_state and st.session_state[key]:
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


def call_openai_completions(system_message, user_message, chat_history, scoring_instructions=None):
    if scoring_instructions:
        full_system_message = f"{system_message}\n\n{scoring_instructions}"
    else:
        full_system_message = system_message

    openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    llm_configuration = st.session_state["selected_model"]
    response = openai_client.chat.completions.create(
        model=llm_configuration["model"],
        messages=chat_history + [
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
    all_passed = True
    if PHASES[PHASE_NAME].get("scored_phase", False):
        minimum_score = PHASES[PHASE_NAME].get("minimum_score", 1)
        for field_key in PHASES[PHASE_NAME]["fields"]:
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


def main():
    if 'CURRENT_PHASE' not in st.session_state:
        st.session_state['CURRENT_PHASE'] = 0
    if 'results' not in st.session_state:
        st.session_state['results'] = {}
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'selected_model' not in st.session_state:
        st.session_state['selected_model'] = LLM_CONFIGURATION["gpt-4o"]

    st.title("Critical Analysis of Video Engagement in Online Education")
    st.markdown(
        "Welcome to the critical analysis exercise. We'll go through the paper step by step, analyzing its key components.")

    with st.sidebar:
        st.header("LLM Configuration")
        model_name = st.selectbox("Select Model", options=list(LLM_CONFIGURATION.keys()))
        st.session_state['selected_model'] = LLM_CONFIGURATION[model_name]
        config = st.session_state['selected_model']

        config["temperature"] = st.slider(f"Temperature ({model_name})", 0.0, 1.0, float(config["temperature"]),
                                          step=0.01)
        config["top_p"] = st.slider(f"Top P ({model_name})", 0.0, 1.0, float(config["top_p"]), step=0.01)
        config["max_tokens"] = st.number_input(f"Max Tokens ({model_name})", 1, 4096, int(config["max_tokens"]))
        config["frequency_penalty"] = st.slider(f"Frequency Penalty ({model_name})", 0.0, 1.0,
                                                float(config["frequency_penalty"]), step=0.01)
        config["presence_penalty"] = st.slider(f"Presence Penalty ({model_name})", 0.0, 1.0,
                                               float(config["presence_penalty"]), step=0.01)

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
                if key in st.session_state:
                    st.info(st.session_state[key], icon="🤖")

        if submit_button:
            for field_key, field in fields.items():
                st_store(user_input[field_key], PHASE_NAME, field_key, "user_input")
                user_response = user_input[field_key]
                system_instructions = PHASE_DICT.get("system_instructions", "")
                rubric = PHASE_DICT.get("rubric", "")
                scored_phase = PHASE_DICT.get("scored_phase", False)

                scoring_instructions = build_scoring_instructions(rubric) if scored_phase else None
                chat_history = st.session_state.get('chat_history', [])

                if scored_phase:
                    # Get the score response
                    score_response = call_openai_completions(system_instructions, user_response, chat_history,
                                                             scoring_instructions)
                    st.session_state['chat_history'].append({"role": "user", "content": user_response})
                    st.session_state['chat_history'].append({"role": "assistant", "content": score_response})
                    st_store(score_response, PHASE_NAME, field_key, "ai_score_response")

                    score = extract_score(score_response)
                    st_store(score, PHASE_NAME, field_key, "ai_score")

                    # Get the feedback response
                    feedback_response = call_openai_completions(system_instructions, user_response,
                                                                st.session_state['chat_history'])
                    st.session_state['chat_history'].append({"role": "assistant", "content": feedback_response})
                    st_store(feedback_response, PHASE_NAME, field_key, "ai_response")

                    feedback_message = f"""
                                        AI Score Feedback: {score_response}\n
                                        AI Feedback: {feedback_response}\n
                                        Score: {score}
                                        """
                    st.success(feedback_message)
                else:
                    feedback_response = call_openai_completions(system_instructions, user_response, chat_history)
                    st.session_state['chat_history'].append({"role": "user", "content": user_response})
                    st.session_state['chat_history'].append({"role": "assistant", "content": feedback_response})
                    st_store(feedback_response, PHASE_NAME, field_key, "ai_response")

                    feedback_message = f"""
                                        AI Feedback: {feedback_response}
                                        """
                    st.success(feedback_message)

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
            st.success("Congratulations, you have completed the analysis!")
            if True:
                celebration()

        i = min(i + 1, len(PHASES))


if __name__ == "__main__":
    main()
