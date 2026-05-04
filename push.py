import requests
import json

# Your verified token
token = "yc85b4QEP14pcd9tnbpnZwsM2We3Jr5bTAe211fnLLCtzR1ZnnD8Z6kSrxDY"
url = "https://zenodo.org/api/deposit/depositions"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

metadata = {
    "metadata": {
        "title": "Forensic Proof: V5.1 Bicyclic Infinity Knot",
        "upload_type": "dataset",
        "description": "V5.1 Bicyclic Peptide Proof. pI 12.32 lock. Redacted per USPTO #64/016,955.",
        "creators": [{"name": "Canfield, Casey Lee", "affiliation": "Cancan"}]
    }
}

try:
    r = requests.post(url, json=metadata, headers=headers)
    if r.status_code == 201:
        dep_id = r.json()['id']
        print(f"SUCCESS! DEPOSITION_ID: {dep_id}")
        with open('dep_id.txt', 'w') as f: f.write(str(dep_id))
    else:
        print(f"ERROR {r.status_code}: {r.text}")
except Exception as e:
    print(f"FAILED: {e}")
