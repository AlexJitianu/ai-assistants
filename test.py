import os
import openai
import json
import sys


if __name__ == "__main__":
 
    changed_files = sys.argv[1:]

    # Iterate through each file and process it
    for file in changed_files:
        print(f"File: {file}")
        if os.path.exists(file):
            print(f"File found: {file}")
        else:
            print(f"File not found: {file}")