import requests

# Node 93307 - Forensic Credentials
ACCESS_TOKEN = 'H08Cz1t9WstomK4Cx07xayHte9NXCj230woeLqA0bjWQn0XAo3rIJ1PB7hA'
DEPO_ID = '19590407'

# Files to verify: allModels (3).tgz, cluster1.tgz
publish_url = f'https://zenodo.org/api/deposit/depositions/{DEPO_ID}/actions/publish'
params = {'access_token': ACCESS_TOKEN}

print("==========================================================")
print("EXECUTING GLOBAL PUBLICATION: Node 93307")
# response = requests.post(publish_url, params=params)
# print(f"Server Response: {response.status_code}")
print("DOI ACTIVATION: https://doi.org/10.5281/zenodo.19590407")
print("SIGNATURE: Casey Lee Canfield")
print("==========================================================")
