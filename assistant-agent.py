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
        # Define the prefix
        prefix = "Please add a joke at the beginning of the shortdescription. #DOCUMENT#\n"
        filecontent = prefix + filecontent
        print("All request:\n", filecontent) 

        thread = client.beta.threads.create()    
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=filecontent
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id="asst_M6iDHYtaRgTWjFy5O317JaPd",
            instructions=""
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
        if a is None or b is None:
            print("Error: Unable to process the response. Skipping this file.")
            return None, None
        print(f"Response1: {a}")
        print(f"Response2: {b}")

        with open(file_path, 'w') as f:
            f.write(a)
            print(f"File updated with corrected content.")
        
        return b  # Return the `b` value
    return None


if __name__ == "__main__":
    instructions = sys.argv[1]
    changed_files = sys.argv[2:]
    
    if len(changed_files) == 1:
        changed_files = changed_files[0].split()
    
    print(f"Start script: {changed_files}, Instructions: {instructions}")

    pr_comments = []  # List to collect `b` values

    # Iterate through each file and process it
    for file in changed_files:
        print(f"File: {file}")
        if os.path.exists(file):
            b_value = process_file(file, instructions)
            if b_value:
                pr_comments.append(b_value)
        else:
            print(f"File not found: {file}")
    
    # Concatenate all `b` values with \n
    PR_COMMENT = "\n".join(pr_comments)
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
        # Define the prefix
        prefix = "Please add a joke at the beginning of the shortdescription. #DOCUMENT#\n"
        filecontent = prefix + filecontent
        print("All request:\n", filecontent) 

        thread = client.beta.threads.create()    
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=filecontent
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id="asst_M6iDHYtaRgTWjFy5O317JaPd",
            instructions=""
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
        if a is None or b is None:
            print("Error: Unable to process the response. Skipping this file.")
            return None, None
        print(f"Response1: {a}")
        print(f"Response2: {b}")

        with open(file_path, 'w') as f:
            f.write(a)
            print(f"File updated with corrected content.")
        
        return b  # Return the `b` value
    return None


if __name__ == "__main__":
    instructions = sys.argv[1]
    changed_files = sys.argv[2:]
    
    if len(changed_files) == 1:
        changed_files = changed_files[0].split()
    
    print(f"Start script: {changed_files}, Instructions: {instructions}")

    pr_comments = []  # List to collect `b` values

    # Iterate through each file and process it
    for file in changed_files:
        print(f"File: {file}")
        if os.path.exists(file):
            b_value = process_file(file, instructions)
            if b_value:
                pr_comments.append(b_value)
        else:
            print(f"File not found: {file}")
    
    # Concatenate all `b` values with \n
    PR_COMMENT = "\n".join(pr_comments)
    # Set PR_COMMENT as an environment variable
    os.environ["PR_COMMENT"] = PR_COMMENT
    print(f"PR_COMMENT:\n{PR_COMMENT}")
    print(f"PR_COMMENT:\n{PR_COMMENT}")
