import requests
import json

# Replace with your actual OpenProtein API Key
API_KEY = 'YOUR_ACTUAL_KEY_HERE'
URL = 'https://api.openprotein.ai/v1/predict/stability'

payload = {
    "sequences": [
        {"id": "CRC-22", "sequence": "GWLiSVEPGAkLLRTGPvCCVF"},
        {"id": "NC-7", "sequence": "GRKWFDV"}
    ],
    "options": {"chiral_correction": True}
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("Sending sequences to OpenProtein for Stability Scoring...")
r = requests.post(URL, headers=headers, json=payload)
print(r.json())
print("Interface Ready. Add your API Key to execute.")
