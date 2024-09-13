import os
import openai

# Load your OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def call_openai_assistant(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4o-mini",  # Use your desired engine/model
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    prompt = "Hello, OpenAI assistant! How are you?"
    result = call_openai_assistant(prompt)
    print(f"Response: {result}")