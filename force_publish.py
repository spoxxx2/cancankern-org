import requests

ACCESS_TOKEN = 'H08Cz1t9WstomK4Cx07xayHte9NXCj230woeLqA0bjWQn0XAo3rIJ1PB7hA'
DEPO_ID = '19590407'

# Use Bearer Token for API-level authorization
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}/actions/publish'

print("==========================================================")
print(f"INITIATING GLOBAL UPLINK FOR DOI 10.5281/zenodo.{DEPO_ID}")

response = requests.post(url, headers=headers)

if response.status_code == 202:
    print("SUCCESS: Excalibur Protocol V6.1 is now LIVE.")
    print(f"URL: https://doi.org/10.5281/zenodo.{DEPO_ID}")
else:
    print(f"FAILED: {response.status_code}")
    print(f"MESSAGE: {response.text}")

print("SIGNATURE: Casey Lee Canfield")
print("==========================================================")
