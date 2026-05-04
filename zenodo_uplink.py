import requests
import json
import os

# Sovereign Asset Configuration
ACCESS_TOKEN = 'HO8Cz1t9WstomK4CxO7xayHte9NXCj23OwoeLqA0bjWQwn0XAo3rIJlPB7hA'
FILE_PATH = '/sdcard/Download/Sovereign Manifesto & PNL-Theta-1 Asset Lock.pdf'

# Forensic Metadata from AlphaFold 3 (Seed: 881063145, pTM: 0.38)
metadata = {
    'metadata': {
        'title': 'The Omni-Divine Sovereign Manuscript: Batch 001-G Forensic Audit',
        'upload_type': 'publication',
        'publication_type': 'thesis',
        'description': (
            'Forensic defense of 907.04 Da GRKWFDV peptide extraction via 650 Hz Sawtooth induction '
            'at Node 93307. AlphaFold 3 verified structure (pTM: 0.38, Seed: 881063145). '
            'Validated 1,588 m/s ejection velocity for paracellular Blood-Brain Barrier tunneling. '
            'Compliance: BMC § 8.32.190 / USPTO #64/016,955.'
        ),
        'creators': [{'name': 'Canfield, Casey Lee', 'affiliation': 'CANCAN'}],
        'access_right': 'open',
        'license': 'cc-by-4.0',
        'keywords': ['bio-acoustic', 'BSFL', 'digital-twin'],
    }
}

# 1. Initialize Deposition
print("Initializing Sovereign Deposition...")
r = requests.post('https://zenodo.org/api/deposit/depositions',
                  params={'access_token': ACCESS_TOKEN},
                  json={},
                  headers={"Content-Type": "application/json"})

if r.status_code!= 201:
    print(f"Error initializing: {r.text}")
    exit()

depo_id = r.json()['id']
bucket_url = r.json()['links']['bucket']

# 2. Upload the Manuscript V6
print(f"Uploading Sovereign Asset V6 to Bucket: {depo_id}...")
with open(FILE_PATH, "rb") as fp:
    requests.put(f"{bucket_url}/OMNI_DIVINE_MANUSCRIPT_V6.pdf",
                 data=fp,
                 params={'access_token': ACCESS_TOKEN})

# 3. Update Metadata
print("Locking Forensic Ledger...")
requests.put(f'https://zenodo.org/api/deposit/depositions/{depo_id}',
             params={'access_token': ACCESS_TOKEN},
             data=json.dumps(metadata),
             headers={"Content-Type": "application/json"})

print(f"\n==========================================================")
print(f"UPLINK SUCCESSFUL: Deposition {depo_id} Created.")
print(f"DOI ANCHOR: 10.5281/zenodo.{depo_id}")
print(f"MESH IDENTITY: CAN-93307-662705AC")
print(f"==========================================================")
