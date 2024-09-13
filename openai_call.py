import os
import openai
import json

openai.api_key = os.environ['OPENAI_API_KEY']

# new
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

def call_openai_assistant(prompt):
    try:
        client = OpenAI()
        response = client.chat.completions.create(
          messages=[
            {
              "role": "user",
              "content": "Say this is a test",
            }
          ],
          model="gpt-3.5-turbo",
)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    prompt = "Hello, OpenAI assistant! How are you?"
    result = call_openai_assistant(prompt)
    print(f"Response: {result}")