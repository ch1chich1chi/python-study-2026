import os

from openai import OpenAI

from config import API_KEY_ENV_NAME, BASE_URL, MODEL_NAME


def create_deepseek_client():
    return OpenAI(
        api_key=os.environ.get(API_KEY_ENV_NAME),
        base_url=BASE_URL,
    )


def stream_chat_response(messages):
    client = create_deepseek_client()
    return client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )