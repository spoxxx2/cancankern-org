import requests
import json
import os

# Hardwired Token from Casey Node
ACCESS_TOKEN = 'mlYoPHFkMXX8pdOlkLWERcCFoPhWWoJDsIY3cXyhewgzl1kFfVAgNSrK0vtD'

def upload_to_zenodo(batch_file):
    headers = {"Content-Type": "application/json"}
    params = {'access_token': ACCESS_TOKEN}
    
    # 1. Create deposition
    r = requests.post('https://zenodo.org/api/deposit/depositions',
                      params=params, json={}, headers=headers)
    
    if r.status_code != 201:
        print(f"Error creating deposition: {r.json()}")
        return

    deposition_data = r.json()
    bucket_url = deposition_data['links']['bucket']
    deposition_id = deposition_data['id']
    
    # 2. Upload the Digital Twin JSON
    filename = os.path.basename(batch_file)
    with open(batch_file, "rb") as fp:
        requests.put(f"{bucket_url}/{filename}", data=fp, params=params)
    
    # 3. Add Forensic Metadata for Dr. Bitan
    data = {
        'metadata': {
            'title': f'Forensic Bio-Acoustic Audit - Node 93307 - {filename}',
            'upload_type': 'dataset',
            'description': 'Automated log of Daughter Peptide induction. Observed Resonant Drag: -1.88Hz. Verified at Panama Lane Node.',
            'creators': [{'name': 'Canfield, Casey Lee', 'affiliation': 'Cancan Kern'}],
            'access_right': 'open',
            'license': 'cc-by-4.0'
        }
    }
    
    final_r = requests.put(f'https://zenodo.org/api/deposit/depositions/{deposition_id}',
                 params=params, data=json.dumps(data), headers=headers)
    
    if final_r.status_code == 200:
        print(f"\n--- ZENODO PUBLISH SUCCESS ---")
        print(f"Digital Twin DOI Link: https://zenodo.org/deposit/{deposition_id}")
    else:
        print(f"Metadata Error: {final_r.json()}")

if __name__ == "__main__":
    log_dir = os.path.expanduser("~/logs")
    if os.path.exists(log_dir):
        logs = [os.path.join(log_dir, f) for f in os.listdir(log_dir) if f.endswith('.json')]
        if logs:
            latest_log = max(logs, key=os.path.getctime)
            upload_to_zenodo(latest_log)
        else:
            print("No logs found in ~/logs/")
    else:
        print("Logs directory not found.")
