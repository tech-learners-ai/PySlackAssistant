
from ..utils import secret as secret
from ..utils.log import log
import openai
import json

def request_text(system_specs, assistant_specs, user_message):
    try:
        openai.api_key = secret.openApi_key
        messages = []
        for content in system_specs:
            messages.append({"role": "system", "content": content})
        for content in assistant_specs:
            messages.append({"role": "assistant", "content": content})
        messages.append({"role": "user", "content": user_message})
        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # log(json.dumps(completion))
        reply = completion.choices[0].message.content
        log(json.dumps(reply))
        return reply
    except Exception as e:
        log(f"Error occurred: {e}")
        return None  # Return None or handle the error as appropriate for your use case