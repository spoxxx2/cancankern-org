import requests

# Node 93307 - Forensic Credentials
ACCESS_TOKEN = 'H08Cz1t9WstomK4Cx07xayHte9NXCj230woeLqA0bjWQn0XAo3rIJ1PB7hA'
DEPO_ID = '19590407'

publish_url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}/actions/publish'
params = {'access_token': ACCESS_TOKEN}

print("==========================================================")
print(f"COMMENCING GLOBAL PUBLICATION FOR NODE 93307")
print(f"TARGET DOI: 10.5281/zenodo.{DEPO_ID}")

# This sends the actual command to make the link live
response = requests.post(publish_url, params=params)

if response.status_code == 202:
    print("SUCCESS: The Excalibur Protocol is now LIVE.")
    print(f"LINK: https://doi.org/10.5281/zenodo.{DEPO_ID}")
else:
    print(f"ERROR: {response.status_code} - Check if files are uploaded.")

print("SIGNATURE: Casey Lee Canfield")
print("==========================================================")
