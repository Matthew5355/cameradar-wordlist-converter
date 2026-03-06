import json
import argparse
import os

# 1. Setup the Command Line Arguments
parser = argparse.ArgumentParser(description='Convert TXT wordlists to Cameradar-compatible JSON.')
parser.add_argument('-f', '--file', required=True, help='Input .txt file (e.g., Hickivision.txt)')
parser.add_argument('-o', '--output', required=True, help='Output .json file name')

args = parser.parse_args()

# 2. Define target usernames
usernames = ['admin', 'root', 'administrator']
credentials_list = []

print(f"--- Starting conversion for: {args.file} ---")

# Check if the input file actually exists
if not os.path.exists(args.file):
    print(f"Error: The file '{args.file}' was not found.")
    exit(1)

try:
    with open(args.file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            password = line.strip()
            if password:
                for user in usernames:
                    credentials_list.append({
                        "username": user,
                        "password": password
                    })

    # 3. Wrap the list in a "credentials" object (Required for Cameradar v6)
    # This fixes the "cannot unmarshal array into Go value" error
    final_json_structure = {
        "credentials": credentials_list
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(final_json_structure, f, indent=2)
        
    print(f"--- Success! Created: {args.output} ---")

except Exception as e:
    print(f"An error occurred: {e}")
