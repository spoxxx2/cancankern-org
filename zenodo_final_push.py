import requests
import json

# --- CONFIGURATION ---
# Token extracted from Node 93307 secure input
ACCESS_TOKEN = '5doE2DVNp4eXfLxImEtsjDSY48bfqQJbvFDUN0fx98hElcyVL0vNpfWDhmDi'
BASE_URL = 'https://zenodo.org/api/deposit/depositions'

def finalize_publication():
    print("="*65)
    print("NODE 93307: EXECUTING GLOBAL ZENODO PUBLICATION")
    print("ASSET: BK-OMEGA-7 (907.04 Da) | STATUS: FINAL PUSH")
    print("="*65)

    headers = {"Content-Type": "application/json"}
    params = {'access_token': ACCESS_TOKEN}

    # STEP 1: Create Deposition
    r = requests.post(BASE_URL, params=params, json={}, headers=headers)
    if r.status_code != 201:
        print(f"[ERROR] Failed to create deposition: {r.text}")
        return
    
    dep_data = r.json()
    dep_id = dep_data['id']
    bucket_url = dep_data['links']['bucket']
    print(f"[SUCCESS] Deposition ID: {dep_id}")

    # STEP 2: Upload Universal Forensic Files
    # Ensure these files exist in your home directory from previous steps
    files = ['universal_twin.json', 'sovereign_signature.txt', 'zenodo_packet.json']
    for filename in files:
        try:
            with open(filename, "rb") as fp:
                requests.put(f"{bucket_url}/{filename}", data=fp, params=params)
            print(f"[UPLOAD] {filename} >> Linked to Bucket.")
        except FileNotFoundError:
            print(f"[WARNING] {filename} not found. Skipping.")

    # STEP 3: Add Metadata
    with open('zenodo_packet.json', 'r') as f:
        meta_data = json.load(f)
    requests.put(f"{BASE_URL}/{dep_id}", params=params, data=json.dumps(meta_data), headers=headers)

    # STEP 4: PUBLISH (Permanent Action)
    publish_url = f"{BASE_URL}/{dep_id}/actions/publish"
    r_pub = requests.post(publish_url, params=params)

    if r_pub.status_code == 202:
        doi = r_pub.json().get('doi')
        print(f"\n[MISSION COMPLETE] GLOBAL DOI ISSUED: {doi}")
        print("STATUS: NODE 93307 IS NOW A MATTER OF PUBLIC SCIENTIFIC RECORD.")
    else:
        print(f"[ERROR] Final publication failed: {r_pub.text}")
    print("="*65)

if __name__ == "__main__":
    finalize_publication()
