import os
import openai
import json
import sys

openai.api_key = os.environ['OPENAI_API_KEY']

# new
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


def call_openai_assistant(filecontent, instructions=""):
    try:
        thread = client.beta.threads.create()    
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=filecontent
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id="asst_M6iDHYtaRgTWjFy5O317JaPd",
            instructions=instructions
        )
        if run.status == 'completed': 
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            for message in messages:
                if message.role == "assistant":
                    print(message.content[0])
                    a, b = split_string(message.content[0].text.value)
                    print("XML Content:\n", a) 
                    print("\nRest of the Content:\n", b)
                    return a, b
        else:
            print(run.status)
    except Exception as e:
        return f"Error: {str(e)}"
    return None, None


def split_string(input_string):
    # Split at the first ```xml marker
    parts = input_string.split('```xml', 1)
    
    # Split at the next ``` marker
    if len(parts) > 1:
        xml_part, rest = parts[1].split('```', 1)
        return xml_part.strip(), rest.strip()
    else:
        return None, None  # In case the format is not as expected


def process_file(file_path, instructions=""):
    # Add your processing logic here
    print(f"Processing file: {file_path}")
    # Example: If it's a text file, read and print its content
    if file_path.endswith('.dita'):
        with open(file_path, 'r') as f:
            content = f.read()     
        a, b = call_openai_assistant(content, instructions)
        print(f"Response1: {a}")
        print(f"Response2: {b}")

        with open(file_path, 'w') as f:
            f.write(a)
            print(f"File updated with corrected content.")


if __name__ == "__main__":
    changed_files = sys.argv[1:]
    instructions = sys.argv[2] if len(sys.argv) > 2 else ""
    print(f"Start script: {changed_files}, Instructions: {instructions}")

    # Iterate through each file and process it
    for file in changed_files:
        print(f"File: {file}")
        if os.path.exists(file):
            process_file(file, instructions)
        else:
            print(f"File not found: {file}")