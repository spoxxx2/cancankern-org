import requests

# Applying New Credential String
ACCESS_TOKEN = 'XBztEuTxjE4hW8zIvOFXtLY1G1AuDUvZv5xOhmtNhuH15Z1q4yHwjjqSkzvh'
DEPO_ID = '19590407'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}/actions/publish'

print("==========================================================")
print(f"INITIATING SOVEREIGN UPLINK: DOI 10.5281/zenodo.{DEPO_ID}")

response = requests.post(url, headers=headers)

if response.status_code == 202:
    print("SUCCESS: Excalibur Protocol V6.1 is officially LIVE.")
    print(f"LINK: https://doi.org/10.5281/zenodo.{DEPO_ID}")
else:
    print(f"STATUS: {response.status_code}")
    print(f"DIAGNOSTIC: {response.text}")

print("SIGNATURE: Casey Lee Canfield")
print("==========================================================")
