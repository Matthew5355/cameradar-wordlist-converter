import json
import argparse
import os

# 1. Setup the Command Line Arguments
parser = argparse.ArgumentParser(description='Convert TXT wordlists to Cameradar-compatible JSON.')
parser.add_argument('-f', '--file', required=True, help='Input .txt file (e.g., rockyou.txt)')
parser.add_argument('-o', '--output', required=True, help='Output .json file name')

args = parser.parse_args()

# 2. Define target usernames (Commonly found in Hikvision/Dahua cameras)
# As mentioned in the video, 'admin' is the most common target.
usernames = ['admin', 'root', 'administrator']
credentials = []

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
                # For every password, we create an entry for each username
                for user in usernames:
                    credentials.append({
                        "username": user,
                        "password": password
                    })

    # 3. Save as a JSON array (The format required by Cameradar)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(credentials, f, indent=2)
    
    print(f"Success! Your JSON dictionary is ready: {args.output}")
    print(f"Total combinations generated: {len(credentials)}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
