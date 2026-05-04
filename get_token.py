import os
import json

# Placeholder logic: Replace with your actual MSAL/Refresh logic
# but ensure it outputs ONLY the access_token string to stdout.
def main():
    token_file = 'token.json'
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            data = json.load(f)
            # Adjust key name if your JSON uses something else
            print(data.get('access_token', ''))
    else:
        print("ERROR: token.json not found")

if __name__ == "__main__":
    main()
