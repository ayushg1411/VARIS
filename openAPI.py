import os
import openai
from config import apikey

openai.api_key = os.getenv("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")
openai.api_key = 1

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write an email to my boss for resignation"
    },
    {
      "role": "assistant",
      "content": "write an email to my boss for resignation"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


