import requests

ACCESS_TOKEN = 'H08Cz1t9WstomK4Cx07xayHte9NXCj230woeLqA0bjWQn0XAo3rIJ1PB7hA'
DEPO_ID = '19590407'
params = {'access_token': ACCESS_TOKEN}

# 1. Check File Status
depo_url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}'
r = requests.get(depo_url, params=params)
depo_data = r.json()

print("==========================================================")
print(f"NODE 93307 AUDIT: {depo_data.get('title')}")
print("FILE LIST:")
for file in depo_data.get('files', []):
    print(f"- {file['filename']} ({file['filesize']} bytes) | ID: {file['id']}")

# 2. Attempt Publication if files are present
if len(depo_data.get('files', [])) > 0:
    print("Files detected. Attempting to force global publication...")
    pub_url = f'{depo_url}/actions/publish'
    pub_res = requests.post(pub_url, params=params)
    if pub_res.status_code == 202:
        print("SUCCESS: DOI ACTIVATED.")
    else:
        print(f"STILL LOCKED: Status {pub_res.status_code}")
        print("REASON: Zenodo is likely still processing the large .tgz clusters.")
else:
    print("ALERT: No files found in draft. Upload required before publishing.")

print("SIGNATURE: Casey Lee Canfield")
print("==========================================================")
