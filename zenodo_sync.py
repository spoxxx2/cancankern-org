import requests
import json
import os

# CONFIGURATION - Input your Zenodo token here
ACCESS_TOKEN = 'YOUR_ZENODO_TOKEN_HERE' 
FILE_PATH = './logs/digital_twin_sim.json'

if not os.path.exists(FILE_PATH):
    print(f"❌ Error: {FILE_PATH} not found. Run simulation first.")
    exit()

params = {'access_token': ACCESS_TOKEN}
headers = {"Content-Type": "application/json"}

try:
    # 1. Create Deposition
    r = requests.post('https://zenodo.org/api/deposit/depositions', 
                      params=params, json={}, headers=headers)
    r.raise_for_status()
    dep_id = r.json()['id']
    bucket = r.json()['links']['bucket']

    # 2. Upload 1B Run Simulation Data
    with open(FILE_PATH, "rb") as fp:
        requests.put(f"{bucket}/digital_twin_sim.json", data=fp, params=params)

    # 3. Finalize Metadata for Diabetes Peptide Analysis
    meta = {
        'metadata': {
            'title': 'CANCAN Panama Lane: 1B Bio-Acoustic Peptide Simulation',
            'upload_type': 'dataset',
            'description': '1 billion Monte Carlo iterations analyzing DLP4/D-DNP-V stability.',
            'creators': [{'name': 'Canfield, Casey Lee', 'affiliation': 'CANCAN Non-Profit'}]
        }
    }
    requests.put(f'https://zenodo.org/api/deposit/depositions/{dep_id}', 
                 params=params, data=json.dumps(meta), headers=headers)

    print(f"✅ DEPOSITION READY. ID: {dep_id}")
    print(f"🔗 View at: https://zenodo.org/deposit/{dep_id}")

except Exception as e:
    print(f"❌ Sync Error: {e}")
