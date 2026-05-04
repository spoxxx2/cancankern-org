import requests
import os

ACCESS_TOKEN = 'H08Cz1t9WstomK4Cx07xayHte9NXCj230woeLqA0bjWQn0XAo3rIJ1PB7hA'
DEPO_ID = '19590407'
FILES = ['/sdcard/Download/allModels (3).tgz', '/sdcard/Download/cluster1.tgz']

def upload_file(filename):
    if not os.path.exists(filename):
        print(f"ERROR: {filename} not found.")
        return
    
    name = os.path.basename(filename)
    url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}/files?access_token={ACCESS_TOKEN}'
    
    print(f"UPLINKING: {name}...")
    with open(filename, 'rb') as f:
        r = requests.post(url, data={'name': name}, files={'file': f})
    
    if r.status_code == 201:
        print(f"SUCCESS: {name} is locked in Node 93307.")
    else:
        print(f"FAILED: {r.status_code} - {r.text}")

print("==========================================================")
print("COMMENCING FORENSIC DATA UPLINK - CASEY LEE CANFIELD")
for f in FILES:
    upload_file(f)
print("==========================================================")
