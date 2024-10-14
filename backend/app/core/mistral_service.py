import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "open-mistral-7b"

client = Mistral(api_key=api_key)

def get_chat_response(user_message: str):
    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.choices[0].message.content
