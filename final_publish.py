import requests

# Node 93307 - Forensic Credentials
ACCESS_TOKEN = 'H08Cz1t9WstomK4Cx07xayHte9NXCj230woeLqA0bjWQn0XAo3rIJ1PB7hA'
DEPO_ID = '19590407'
params = {'access_token': ACCESS_TOKEN}

print("==========================================================")
print(f"VERIFYING NODE 93307 ASSETS...")

# 1. Verify Files Exist in the Deposition
depo_url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}'
r = requests.get(depo_url, params=params)

if r.status_code == 200:
    data = r.json()
    files = data.get('files', [])
    if not files:
        print("ALERT: No files detected. Ensure PDF and .tgz clusters are uploaded.")
    else:
        print(f"FILES DETECTED: {[f['filename'] for f in files]}")
        
        # 2. Trigger Global Publication
        print("PUBLISHING TO GLOBAL HANDLE SERVERS...")
        pub_url = f'{depo_url}/actions/publish'
        p_res = requests.post(pub_url, params=params)
        
        if p_res.status_code == 202:
            print("SUCCESS: Excalibur Protocol V6.1 is now LIVE.")
            print(f"DOI LINK: https://doi.org/10.5281/zenodo.{DEPO_ID}")
        else:
            print(f"FAILED: {p_res.status_code} - {p_res.text}")
else:
    print(f"ERROR: Could not access deposition {DEPO_ID}. Check Access Token.")

print("SIGNATURE: Casey Lee Canfield")
print("==========================================================")
