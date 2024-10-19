import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "open-mixtral-8x22b"

client = Mistral(api_key=api_key)

def get_chat_response(user_message: str, initial_promt: str = None):
    if initial_promt:
        print("initial_promt", initial_promt)
        response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": initial_promt},
                {"role": "user", "content": user_message}],
        )
    else:
        response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": user_message}],
        )
    return response.choices[0].message.content
