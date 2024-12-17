from openai import OpenAI

import json
import os
from dotenv import load_dotenv
import re

#+++++++++CONFIGS++++++++
model_to_use = 'gpt-4o-mini'
#The model to use, gpt 4o mini is usually good enough
number_to_generate = 3
#Number of entries to generate (note, if you disable permit_fail_retry, failed responses will NOT be compensated, and the actual # of entries may be lower than this)

instruction_path = 'instruction.txt'
#path for ai instructions
output_path = 'dataset.json'
#path for dataset output

permit_fail_retry = True
#if regex parsing fails, should the code compensate by trying again?
max_retry_before_abort = 10
#good idea to limit this, as you will be making infinite requests if your instructions is buggy. Generally its good to limit this to 1 per 20 entries.
#++++++++END OF CONFIGS+++++++

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

load_dotenv()


def load_instructions(filename):
    with open(filename, "r") as file:
        return file.readlines()

def generate_entry(instruction):
    prompt = f"{instruction}"
    
    completion = client.chat.completions.create(
        model=model_to_use,
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    raw_output = completion.choices[0].message.content
    print(raw_output)
    
    pattern = r'instruction: \[(.*?)\]\s*input: \[(.*?)\]\s*output: \[(.*?)\]'
    match = re.search(pattern, raw_output, re.DOTALL)

    if match:
        instruction = match.group(1).strip()
        input_data = match.group(2).strip()
        output_data = match.group(3).strip()

        entry = {
            "instruction": instruction,
            "input": input_data,
            "output": output_data
        }
        
        return entry

    else:
        return False

def write_to_json(data, filename):
    file_exists = os.path.exists(filename)
    
    with open(filename, "a") as file:
        if not file_exists or os.stat(filename).st_size == 0:
            file.write("[")
        else:
            file.write(",")
        
        # Write the new data
        json.dump(data, file)
        

def generate_dataset(num_entries):
    instructions = load_instructions(instruction_path)

    successful_entries = 0
    failed_entries = 0

    i = 0
    while successful_entries < num_entries:

        instruction = instructions[i % len(instructions)]

        entry = generate_entry(instructions)

        if entry:
            write_to_json(entry, output_path)
            successful_entries += 1
            print(f"Entry {successful_entries} completed and written to file. {num_entries - successful_entries} more entries to go.\n")
        elif permit_fail_retry:
            failed_entries += 1
            if failed_entries >= max_retry_before_abort:
                print("\n\n\n===============\nABNORMAL EXIT WARN\nMAX RETRIES REACHED\n===============")
                return
            print(f"Entry {successful_entries + 1} failed to generate. Currently have {failed_entries} failed. Retrying...\n")
        else:
            print(f"Entry {successful_entries + 1} failed to generate. No attempts will be made to compensate.\n")
            successful_entries += 1
        i += 1

if __name__ == "__main__":
    generate_dataset(number_to_generate)

    with open(output_path, "a") as file:
            file.write("]")
    
    print("Dataset generation complete!")
