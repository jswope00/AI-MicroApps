import openai
import anthropic
import google.generativeai as genai
import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()

def get_api_key(service_name):
    """Retrieve API key from environment variables based on service name."""
    env_var_name = f"{service_name.upper()}_API_KEY"
    api_key = os.getenv(env_var_name)

    if not api_key:
        raise ValueError(f"API key for {service_name} not found in environment variables.")

    return api_key

# formatting.py
def format_chat_history(chat_history, family):
    """Format chat history based on LLM family."""
    formatted_history = []
    if len(chat_history) > 0:
        for history in chat_history:
            user_content = history["user"]
            assistant_content = history["assistant"]
            if family == "gemini":
                formatted_history.extend([
                    {"role": "user", "parts": [user_content]},
                    {"role": "model", "parts": [assistant_content]}
                ])

            else:
                formatted_history.extend([
                    {"role": "user", "content": user_content},
                    {"role": "assistant", "content": assistant_content}
                ])
    return formatted_history

def handle_openai(context):
    """Handle requests for OpenAI models."""
    if not context["supports_image"] and context.get("image_urls"):
        return "Images are not supported by selected model."
    try:
        openai.api_key = get_api_key("openai")

        messages = format_chat_history(context["chat_history"], "openai") + [
            {"role": "system", "content": context["SYSTEM_PROMPT"]},
            {"role": "assistant", "content": context["phase_instructions"]},
            {"role": "user", "content": context["user_prompt"]}
        ]

        if context["supports_image"] and context["image_urls"]:
            messages.insert(2, {"role": "user", "content": [{"type": "image_url", "image_url": {"url": url}} for url in
                                                            context["image_urls"]]})

        response = openai.chat.completions.create(
            model=context["model"],
            messages=messages,
            temperature=context["temperature"],
            max_tokens=context["max_tokens"],
            top_p=context["top_p"],
            frequency_penalty=context["frequency_penalty"],
            presence_penalty=context["presence_penalty"]
        )

        input_price = int(response.usage.prompt_tokens) * context["price_input_token_1M"] / 1000000
        output_price = int(response.usage.completion_tokens) * context["price_output_token_1M"] / 1000000
        total_price = input_price + output_price
        context['TOTAL_PRICE'] += total_price

        return response.choices[0].message.content

    except Exception as e:
        return f"Unexpected error while handling OpenAI request: {e}"

def handle_claude(context):
    """Handle requests for Claude models."""
    if not context["supports_image"] and context.get("image_urls"):
        return "Images are not supported by selected model."
    try:
        client = anthropic.Anthropic(api_key=get_api_key("claude"))

        messages = format_chat_history(context["chat_history"], "claude") + [
            {"role": "user", "content": [{"type": "text", "text": context["user_prompt"]}]},
            {"role": "assistant", "content": [{"type": "text", "text": context["phase_instructions"]}]}
        ]

        if context["supports_image"] and context["image_urls"]:
            for image_url in context["image_urls"]:
                # Extract base64 data from the image URL
                base64_data = image_url.split(",")[1]
                mime_type = re.search(r"data:(.*?);base64,", image_url).group(1) if re.search(r"data:(.*?);base64,", image_url) else None
                # Add image to the messages
                messages.append({
                    "role": "user",
                    "content": [{
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": mime_type,
                            "data": base64_data
                        }
                    }]
                })

        response = client.messages.create(
            model=context["model"],
            max_tokens=context["max_tokens"],
            temperature=context["temperature"],
            system=f"{context['SYSTEM_PROMPT']}",
            messages=messages
        )

        input_price = int(response.usage.input_tokens) * context["price_input_token_1M"] / 1000000
        output_price = int(response.usage.output_tokens) * context["price_output_token_1M"] / 1000000
        total_price = input_price + output_price
        context['TOTAL_PRICE'] += total_price

        return '\n'.join([block.text for block in response.content if block.type == 'text'])

    except Exception as e:
        return f"Unexpected error while handling Claude request: {e}"

def handle_gemini(context):
    """Handle requests for Gemini models."""
    if not context["supports_image"] and context.get("image_urls"):
        return "Images are not supported by selected model."
    try:
        genai.configure(api_key=get_api_key("google"))

        messages = format_chat_history(context["chat_history"], "gemini") + [
            {"role": "user", "parts": [context["user_prompt"]]}
        ]

        if context["supports_image"] and context["image_urls"]:
            for image_url in context["image_urls"]:
                messages.append({
                    "role": "user",
                    "parts": [{
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_url
                        }
                    }]
                })

        chat_session = genai.GenerativeModel(
            model_name=context["model"],
            generation_config={
                "temperature": context["temperature"],
                "top_p": context["top_p"],
                "max_output_tokens": context["max_tokens"],
                "response_mime_type": "text/plain"
            }
        ).start_chat(history=messages)

        response = chat_session.send_message(context["user_prompt"])

        return response.text

    except Exception as e:
        return f"Unexpected error while handling Gemini request: {e}"

def handle_perplexity(context):
    """Handle requests for Perplexity models."""
    if not context["supports_image"] and context.get("image_urls"):
        return "Images are not supported by selected model."
    api_key = get_api_key("perplexity")
    url = "https://api.perplexity.ai/chat/completions"

    # Prepare messages
    messages = [
        {"role": "system", "content": context["SYSTEM_PROMPT"] + context["phase_instructions"]}
    ] + format_chat_history(context["chat_history"], "perplexity") + [
        {"role": "user", "content": context["user_prompt"]}
    ]

    # Add image URLs if supported
    if context["supports_image"] and context["image_urls"]:
        for image_url in context["image_urls"]:
            messages.append({
                "role": "user",
                "content": {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                }
            })

    # Prepare payload
    payload = {
        "model": context["model"],
        "messages": messages
    }

    # Prepare headers
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}"
    }

    # Make the API request
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        response_json = response.json()
        if "choices" in response_json and len(response_json["choices"]) > 0:
            return response_json["choices"][0]["message"]["content"]
        else:
            return "Unexpected response format from Perplexity API."

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred while handling Perplexity request: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Error occurred while making the Perplexity request: {req_err}"


# Mapping of model families to handler functions
HANDLERS = {
    "openai": handle_openai,
    "claude": handle_claude,
    "gemini": handle_gemini,
    "perplexity":handle_perplexity
}
