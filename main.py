import os
import importlib
import copy
import re
from llm_config import LLM_CONFIG
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.let_it_rain import rain
import base64
from handlers import HANDLERS
import mimetypes

# Define templates for different configurations
templates = {
    "Alt Text Generator": "config_alt_text",
    "Case Study: Ebola": "config_ebola_case_study",
    "Demo 1": "config_demo1",
    "Demo 2": "config_demo2",
    "ai_assessment": "config",
    "MCQ Generator": "config_mcq_generator",
    "Debate an AI": "config_debate",
    "mSCT Tutor": "config_msct_tutor",
    "Find the Incorrect Fact": "config_incorrect_fact",
    "SOAP Notes Scoring": "config_soap",
    "Question Feedback Generator": "config_question_feedback",
    "Learning Objective Generator": "config_lo_generator",
    "Image Quiz": "config_image_quiz",
    "Zodiac Symbol": "config_zodiac",
    "Career Advisor": "config_career_path"
}

# Select template from the sidebar
selected_template = st.sidebar.selectbox("Select template", templates.keys())

if "template" not in st.session_state or st.session_state.template != selected_template:
    st.session_state.template = selected_template
    st.query_params["template"] = selected_template
    # Clear all session state variables
    keys_to_keep = ['template']  # Add any other keys you want to preserve
    for key in list(st.session_state.keys()):
        if key not in keys_to_keep:
            del st.session_state[key]
    st.session_state['additional_prompt'] = ""
    st.session_state['chat_history'] = []
    st.session_state['CURRENT_PHASE'] = 0
    st.session_state['TOTAL_PRICE'] = 0

    st.rerun()

config_file = templates[selected_template]

if config_file:
    config_module = importlib.import_module(config_file)
    for attr in dir(config_module):
        if not attr.startswith("__"):
            globals()[attr] = getattr(config_module, attr)
else:
    from config import *

def merge_configurations(defaults, overrides):
    merged = copy.deepcopy(defaults)
    for key, override_values in overrides.items():
        if key in merged:
            merged[key].update(override_values)
        else:
            merged[key] = override_values
    return merged

LLM_CONFIGURATIONS = merge_configurations(LLM_CONFIG, LLM_CONFIG_OVERRIDE)


user_input = {}
function_map = {
    "text_input": st.text_input,
    "text_area": st.text_area,
    "warning": st.warning,
    "button": st.button,
    "radio": st.radio,
    "markdown": st.markdown,
    "selectbox": st.selectbox,
    "checkbox": st.checkbox,
    "slider": st.slider,
    "number_input": st.number_input,
    "image": st.image,
    "file_uploader": st.file_uploader
}


def evaluate_conditions(user_input, condition):
    """Evaluate whether a user_input meets the specified condition."""
    if "$and" in condition:
        return all(evaluate_conditions(user_input, sub_condition) for sub_condition in condition["$and"])
    elif "$or" in condition:
        return any(evaluate_conditions(user_input, sub_condition) for sub_condition in condition["$or"])
    elif "$not" in condition:
        return not evaluate_conditions(user_input, condition["$not"])

    for key, value in condition.items():
        if isinstance(value, dict):
            operator, condition_value = next(iter(value.items()))
            user_value = user_input.get(key)

            if operator == "$gt" and not user_value > condition_value:
                return False
            elif operator == "$lt" and not user_value < condition_value:
                return False
            elif operator == "$gte" and not user_value >= condition_value:
                return False
            elif operator == "$lte" and not user_value <= condition_value:
                return False
            elif operator == "$eq" and not user_value == condition_value:
                return False
            elif operator == "$ne" and not user_value != condition_value:
                return False
            elif operator == "$in" and user_value not in condition_value:
                return False
            elif operator == "$nin" and user_value in condition_value:
                return False
        else:
            if isinstance(value, list):
                if user_input.get(key) not in value:
                    return False
            else:
                if user_input.get(key) != value:
                    return False
    return True

def build_field(phase_name, fields):
    for field_key, field in fields.items():
        # Check showIf conditions
        if 'showIf' in field:
            condition = field['showIf']
            if not evaluate_conditions(user_input, condition):
                continue
        field_type = field.get("type", "")
        field_label = field.get("label", "")
        field_body = field.get("body", "")
        field_value = field.get("value", "")
        field_index = field.get("index",None)
        field_max_chars = field.get("max_chars", None)
        field_help = field.get("help", "")
        field_on_click = field.get("on_click", None)
        field_options = field.get("options", [])
        field_horizontal = field.get("horizontal", False)
        field_min_value = field.get("min_value",None)
        field_max_value = field.get("max_value",None)
        field_step = field.get("step",None)
        field_height = field.get("height", None)
        field_unsafe_html = field.get("unsafe_allow_html", False)
        field_placeholder = field.get("placeholder", "")
        field_image = field.get("image", "")
        field_caption = field.get("caption", "")
        field_allowed_files = field.get("allowed_files", None)
        field_multiple_files = field.get("multiple_files", False)
        field_label_visibility = field.get("label_visibility", None)

        kwargs = {}
        if field_label:
            kwargs['label'] = field_label
        if field_body:
            kwargs['body'] = field_body
        if field_value:
            kwargs['value'] = field_value
        if field_index:
            kwargs['index'] = field_index
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
        if field_min_value:
            kwargs['min_value'] = field_min_value
        if field_max_value:
            kwargs['max_value'] = field_max_value
        if field_step:
            kwargs['step'] = field_step
        if field_height:
            kwargs['height'] = field_height
        if field_unsafe_html:
            kwargs['unsafe_allow_html'] = field_unsafe_html
        if field_placeholder:
            kwargs['placeholder'] = field_placeholder
        if field_image:
            kwargs['image'] = field_image
        if field_caption:
            kwargs['caption'] = field_caption
        if field_allowed_files:
            kwargs['type'] = field_allowed_files
        if field_multiple_files:
            kwargs['accept_multiple_files'] = field_multiple_files
        if field_label_visibility:
            kwargs['label_visibility'] = field_label_visibility

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

                div[role="radiogroup"] label p{
                    font-weight: unset !important;
                    font-size: unset !important;
                }
                """,
        ):
            user_input[field_key] = my_input_function(**kwargs)

def execute_llm_completions(selected_llm, phase_instructions, user_prompt, image_urls=None):
    """Execute LLM completions using the selected model."""
    if selected_llm not in LLM_CONFIG:
        raise ValueError(f"Selected model '{selected_llm}' not found in configuration.")

    model_config = LLM_CONFIG[selected_llm]
    family = model_config["family"]
    chat_history = st.session_state["chat_history"]

    context = {
        "SYSTEM_PROMPT": SYSTEM_PROMPT,
        "phase_instructions": phase_instructions,
        "user_prompt": user_prompt,
        "supports_image": model_config["supports_image"],
        "image_urls": image_urls,
        "model": model_config["model"],
        "max_tokens": model_config["max_tokens"],
        "temperature": model_config["temperature"],
        "top_p": model_config["top_p"],
        "frequency_penalty": model_config["frequency_penalty"],
        "presence_penalty": model_config["presence_penalty"],
        "price_input_token_1M": model_config["price_input_token_1M"],
        "price_output_token_1M": model_config["price_output_token_1M"],
        "TOTAL_PRICE": 0,
        "chat_history": chat_history
    }

    handler = HANDLERS.get(family)
    if handler:
        try:
            result = handler(context)
        except Exception as e:
            raise RuntimeError(f"Error in handling the LLM request: {e}")
    else:
        raise NotImplementedError(f"No handler implemented for model family '{family}'")
    return result

def prompt_conditionals(user_input, phase_name=None):
    phase = PHASES[phase_name]
    if isinstance(phase["user_prompt"], str):
        base_prompt = phase["user_prompt"]
    else:
        additional_prompts = []
        for item in phase["user_prompt"]:
            condition_clause = item["condition"]
            if evaluate_conditions(user_input, condition_clause):
                additional_prompts.append(item["prompt"])
        base_prompt = "\n".join(additional_prompts)
    return base_prompt

def format_user_prompt(prompt, user_input, phase_name=None):
    try:
        # Apply conditional logic to determine the correct prompt based on user_input and phase_name
        prompt = prompt_conditionals(user_input, phase_name)
        # Safely format the prompt using the keys that are actually in user_input
        formatted_user_prompt = prompt.format(**{k: user_input.get(k, '') for k in re.findall(r'{(\w+)}', prompt)})
        return formatted_user_prompt
    except Exception as e:
        print("Error occurred:", e)
        formatted_user_prompt = prompt.format(**user_input)
        return formatted_user_prompt


def st_store(input, phase_name, phase_key, field_key=""):
    if field_key:
        key = f"{phase_name}_{field_key}_{phase_key}"
    else:
        key = f"{phase_name}_{phase_key}"
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


def check_score(PHASE_NAME):
    score = st.session_state[f"{PHASE_NAME}_ai_score"]
    try:
        if score >= PHASES[PHASE_NAME]["minimum_score"]:
            st.session_state[f"{PHASE_NAME}_phase_status"] = True
            return True
        else:
            st.session_state[f"{PHASE_NAME}_phase_status"] = False
            return False
    except:
        st.session_state[f"{PHASE_NAME}_phase_status"] = False
        return False


def skip_phase(PHASE_NAME, No_Submit=False):
    phase_fields = PHASES[PHASE_NAME]["fields"]
    for field_key in phase_fields:
        st_store(user_input[field_key], PHASE_NAME, "user_input", field_key)
    if not No_Submit:
        st.session_state[f"{PHASE_NAME}_ai_response"] = "This phase was skipped."
    st.session_state[f"{PHASE_NAME}_phase_status"] = True
    st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)


def celebration():
    rain(
        emoji="🥳",
        font_size=54,
        falling_speed=5,
        animation_length=1,
    )

# Function to find the image URL
def find_image_urls(fields):
    image_urls = []
    for key, value in fields.items():
        if 'image' in value:
            image_urls.append(value['image'])
        if 'file_uploader' in value.values():
            uploaded_files = user_input[key]
            if not isinstance(uploaded_files, list):
                uploaded_files = [uploaded_files]
            for uploaded_file in uploaded_files:
                if uploaded_file:
                    # Read and encode file content
                    file_content = uploaded_file.read()
                    mime_type, _ = mimetypes.guess_type(uploaded_file.name)
                    if not mime_type:
                        mime_type = 'application/octet-stream'
                    base64_encoded_content = base64.b64encode(file_content).decode('utf-8')
                    image_url = f"data:{mime_type};base64,{base64_encoded_content}"
                    image_urls.append(image_url)
    return image_urls

def main():

    if 'TOTAL_PRICE' not in st.session_state:
        st.session_state['TOTAL_PRICE'] = 0

    with st.sidebar:
        llm_options = list(LLM_CONFIGURATIONS.keys())
        # Find the index of the selected_key in the list of options
        llm_index = llm_options.index(PREFERRED_LLM) if PREFERRED_LLM in llm_options else 0

        selected_llm = st.selectbox("Select Language Model", options=LLM_CONFIGURATIONS.keys(), index=llm_index, key="selected_llm")
        # Get the initial LLM configuration from the selected model
        initial_config = LLM_CONFIGURATIONS[selected_llm]

        # Parameter adjustment inputs
        st.session_state['llm_config'] = {
            "model": initial_config["model"],
            "temperature": st.slider("Temperature", min_value=0.0, max_value=1.0,
                                     value=float(initial_config.get("temperature", 1.0)), step=0.01),
            "max_tokens": st.slider("Max Tokens", min_value=50, max_value=4000,
                                    value=int(initial_config.get("max_tokens", 1000)), step=50),
            "top_p": st.slider("Top P", min_value=0.0, max_value=1.0, value=float(initial_config.get("top_p", 1.0)), step=0.1),
            "frequency_penalty": st.slider("Frequency Penalty", min_value=0.0, max_value=1.0,
                                           value=float(initial_config.get("frequency_penalty", 0.0)), step=0.01),
            "presence_penalty": st.slider("Presence Penalty", min_value=0.0, max_value=1.0,
                                          value=float(initial_config.get("presence_penalty", 0.0)), step=0.01),
            "price_input_token_1M": st.number_input("Input Token Price 1M", value=initial_config.get("price_input_token_1M", 0)),
            "price_output_token_1M": st.number_input("Output Token Price 1M", value=initial_config.get("price_output_token_1M", 0))
        }

        if DISPLAY_COST:
            st.write("Price : ${:.6f}".format(st.session_state['TOTAL_PRICE']))

        with st.sidebar:
            st.subheader("Chat History")
            for history in st.session_state['chat_history']:
                st.markdown(f"**User:** {history['user']}")
                if 'images' in history:
                    for image in history['images']:
                        st.image(image)
                st.markdown(f"**AI:** {history['assistant']}")
                st.markdown("---")

    if 'CURRENT_PHASE' not in st.session_state:
        st.session_state['CURRENT_PHASE'] = 0

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
        skip_button = False
        final_phase_name = list(PHASES.keys())[-1]
        final_key = f"{final_phase_name}_ai_response"

        PHASE_NAME = list(PHASES.keys())[i]
        PHASE_DICT = PHASES[PHASE_NAME]
        fields = PHASE_DICT["fields"]

        st.write(f"#### Phase {i + 1}: {PHASE_DICT['name']}")

        build_field(PHASE_NAME, fields)

        key = f"{PHASE_NAME}_phase_status"

        user_prompt_template = PHASE_DICT.get("user_prompt", "")
        if PHASE_DICT.get("show_prompt", False):
            with st.expander("View/edit full prompt"):
                formatted_user_prompt = st.text_area(
                    label="Prompt",
                    height=100,
                    max_chars=50000,
                    value=format_user_prompt(user_prompt_template, user_input, PHASE_NAME),
                    disabled=PHASE_DICT.get("read_only_prompt",False)
                    )
        else:
            formatted_user_prompt = format_user_prompt(user_prompt_template, user_input, PHASE_NAME)

        if PHASE_DICT.get("no_submission", False):
            if key not in st.session_state:
                st.session_state[key] = True
                st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)
                st.session_state[f"{PHASE_NAME}_phase_completed"] = True
                st.rerun()

        if key not in st.session_state:
            st.session_state[key] = False

        if not st.session_state.get(f"{PHASE_NAME}_phase_completed", False):
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    submit_button = st.button(label=PHASE_DICT.get("button_label", "Submit"), type="primary",
                                              key=f"submit {i}")
                with col2:
                    if PHASE_DICT.get("allow_skip", False):
                        skip_button = st.button(label="Skip Question", key=f"skip {i}")

        key = f"{PHASE_NAME}_ai_response"
        if key in st.session_state and st.session_state[key]:
            st.info(st.session_state[key], icon="🤖")

        key = f"{PHASE_NAME}_ai_score_debug"
        if key in st.session_state and st.session_state[key]:
            st.info(st.session_state[key], icon="🤖")

        key = f"{PHASE_NAME}_ai_response_revision_1"
        # If there are any revisions, enter the loop
        if key in st.session_state and st.session_state[key]:
            z = 1
            while z <= PHASE_DICT.get("max_revisions",10):
                key = f"{PHASE_NAME}_ai_response_revision_{z}"
                if key in st.session_state and st.session_state[key]:
                    st.info(st.session_state[key], icon="🤖")
                z += 1

        if submit_button:
            for field_key, field in fields.items():
                st_store(user_input.get(field_key,""), PHASE_NAME, "user_input", field_key)

            phase_instructions = PHASE_DICT.get("phase_instructions", "")

            image_urls = find_image_urls(PHASE_DICT.get('fields', {}))

            if PHASE_DICT.get("ai_response", True):
                if PHASE_DICT.get("scored_phase", False):
                    if "rubric" in PHASE_DICT:
                        scoring_instructions = build_scoring_instructions(PHASE_DICT["rubric"])
                        ai_feedback = execute_llm_completions(selected_llm,phase_instructions, formatted_user_prompt, image_urls)
                        st.info(body=ai_feedback, icon="🤖")
                        ai_score = execute_llm_completions(selected_llm,scoring_instructions, ai_feedback)
                        st.info(ai_score, icon="🤖")
                        st_store(ai_feedback, PHASE_NAME, "ai_response")
                        st_store(ai_score, PHASE_NAME, "ai_score_debug")
                        score = extract_score(ai_score)
                        st_store(score, PHASE_NAME, "ai_score")
                        chat_history_entry = {
                            "user": formatted_user_prompt,
                            "assistant": ai_feedback
                        }
                        if image_urls:
                            chat_history_entry["images"] = image_urls

                        st.session_state['chat_history'].append(chat_history_entry)
                        st.session_state["ai_score"] = ai_score
                        st.session_state['score'] = score
                        if check_score(PHASE_NAME):
                            st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)
                            st.session_state[f"{PHASE_NAME}_phase_completed"] = True
                            st.rerun()
                        else:
                            st.warning("You haven't passed. Please try again.")
                    else:
                        st.error('You need to include a rubric for a scored phase', icon="🚨")
                else:
                    ai_feedback = execute_llm_completions(selected_llm,phase_instructions, formatted_user_prompt, image_urls)
                    st_store(ai_feedback, PHASE_NAME, "ai_response")
                    chat_history_entry = {
                        "user": formatted_user_prompt,
                        "assistant": ai_feedback
                    }
                    if image_urls:
                        chat_history_entry["images"] = image_urls

                    st.session_state['chat_history'].append(chat_history_entry)
                    st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)
                    st.session_state[f"{PHASE_NAME}_phase_completed"] = True
                    st.rerun()
            else:
                res_box = st.info(body="", icon="🤖")
                result = ""
                hard_coded_message = PHASE_DICT.get('custom_response', None)
                hard_coded_message = format_user_prompt(hard_coded_message, user_input, PHASE_NAME)
                for char in hard_coded_message:
                    result += char
                    res_box.info(body=result, icon="🤖")
                st.session_state[f"{PHASE_NAME}_ai_response"] = hard_coded_message
                chat_history_entry = {
                    "user": formatted_user_prompt,
                    "assistant": hard_coded_message
                }
                if image_urls:
                    chat_history_entry["images"] = image_urls

                st.session_state['chat_history'].append(chat_history_entry)
                st.session_state['CURRENT_PHASE'] = min(st.session_state['CURRENT_PHASE'] + 1, len(PHASES) - 1)
                st.session_state[f"{PHASE_NAME}_phase_completed"] = True
                st.rerun()

        if PHASE_DICT.get("allow_revisions", False):
            if f"{PHASE_NAME}_ai_response" in st.session_state:
                # Check if the current phase is the latest completed phase
                is_latest_completed_phase = i == st.session_state['CURRENT_PHASE'] or (
                            i == st.session_state['CURRENT_PHASE'] - 1 and not st.session_state.get(
                        f"{list(PHASES.keys())[i + 1]}_phase_completed", False))

                # Check if it's not the last phase and the phase wasn't skipped
                is_not_last_phase = PHASE_NAME != final_phase_name
                is_not_skipped = not st.session_state.get(f"{PHASE_NAME}_skipped", False)

                if is_latest_completed_phase and is_not_last_phase and is_not_skipped:
                    with st.expander("Revise this response?"):
                        max_revisions = PHASE_DICT.get("max_revisions", 10)
                        if f"{PHASE_NAME}_revision_count" not in st.session_state:
                            st_store(0, PHASE_NAME, "revision_count")
                        if st.session_state[f"{PHASE_NAME}_revision_count"] < max_revisions:
                            st.session_state['additional_prompt'] = st.text_input("Enter additional prompt", value="",
                                                                                  key=PHASE_NAME)
                            if st.button("Revise", key=f"revise_{i}"):
                                st.session_state[f"{PHASE_NAME}_revision_count"] += 1

                                phase_instructions = PHASE_DICT.get("phase_instructions", "")
                                user_prompt_template = PHASE_DICT.get("user_prompt", "")
                                formatted_user_prompt = format_user_prompt(user_prompt_template, user_input, PHASE_NAME)

                                formatted_user_prompt += st.session_state['additional_prompt']

                                ai_feedback = execute_llm_completions(selected_llm,phase_instructions, formatted_user_prompt)

                                st_store(ai_feedback, PHASE_NAME, "ai_response_revision_" + str(
                                    st.session_state[f"{PHASE_NAME}_revision_count"]))
                                chat_history_entry = {
                                    "user": formatted_user_prompt,
                                    "assistant": ai_feedback
                                }
                                if image_urls:
                                    chat_history_entry["images"] = image_urls

                                st.session_state['chat_history'].append(chat_history_entry)
                                st.rerun()
                        else:
                            st.warning("Revision limits exceeded")

        if skip_button:
            skip_phase(PHASE_NAME)
            st.session_state[f"{PHASE_NAME}_phase_completed"] = True
            st.session_state[f"{PHASE_NAME}_skipped"] = True
            st.rerun()

        if final_key in st.session_state and i == st.session_state['CURRENT_PHASE']:
            st.success(COMPLETION_MESSAGE)
            if COMPLETION_CELEBRATION:
                celebration()

        i = min(i + 1, len(PHASES))



if __name__ == "__main__":
    main()