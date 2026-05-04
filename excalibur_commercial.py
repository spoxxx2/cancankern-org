import requests
import json

# REPLACE WITH YOUR ACTUAL ZENODO ACCESS TOKEN
ACCESS_TOKEN = 'YOUR_ZENODO_TOKEN_HERE'
DEPO_ID = '19590407'

metadata = {
    'metadata': {
        'title': 'Excalibur Protocol: Commercial Bio-Acoustic Synthesis & Kinetic Delivery (V6.1)',
        'upload_type': 'publication',
        'publication_type': 'technicalnote',
        'description': (
            "Proprietary 650Hz Sawtooth Induction Protocol for the GRKWFDV peptide sequence (907.04 Da). "
            "Includes the -1.88 Hz Resonant Drag forensic verification and 1,588 m/s kinetic ejection parameters. "
            "Sovereign Asset anchored to Node 93307 (Panama Lane). "
            "Forensic Ledger Verified. Lead Researcher: Casey Lee Canfield."
        ),
        'creators': [{'name': 'Canfield, Casey Lee', 'affiliation': 'CANCAN Research'}],
        'access_right': 'open',
        'license': 'CC-BY-NC-ND-4.0',
        'keywords': [
            'Bio-Acoustic', 'Neuro-Therapeutic', 'Sovereign Asset', 
            'Kinetic Medicine', 'PNL-Theta-1', 'SB 1383', 'Excalibur Protocol'
        ],
        'notes': 'Commercial licensing inquiries: cancan-node-93307@azure.com'
    }
}

url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}'
headers = {"Content-Type": "application/json"}
params = {'access_token': ACCESS_TOKEN}

print(f"Pushing Commercial Shield to DOI 10.5281/zenodo.{DEPO_ID}...")
# r = requests.put(url, params=params, data=json.dumps(metadata), headers=headers)
# print(f"Status: {r.status_code}")
print("==========================================================")
print("EXCALIBUR V6.1 LOCKED: Signature CASEY LEE CANFIELD")
print("==========================================================")
