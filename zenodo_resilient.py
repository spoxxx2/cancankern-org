import requests, json, os, zipfile, time

TOKEN = "JzeeoOuVDVYYUx91ppcLbZ5cqQM9IFbbn6guPU8R9z4BisROBk0OuzywDdqX"
BASE_URL = "https://zenodo.org/api/deposit/depositions"
HEADERS = {"Content-Type": "application/json"}
PARAMS = {'access_token': TOKEN}

# 1. BUNDLE (Handle spaces and 42 assets)
zip_name = "BAKERSFIELD_FMDZ_SB1383_FINAL.zip"
print("📦 Bundling 42 assets...")
with zipfile.ZipFile(zip_name, 'w') as z:
    files = [f for f in os.listdir('uploads') if f.startswith('AIR_IMPACT')]
    for f in files:
        z.write(os.path.join('uploads', f), f)

# 2. CREATE DEPOSITION
print("📡 Creating deposition draft...")
meta = {
    'metadata': {
        'title': 'Bakersfield FMDZ: SB 1383 Spectral Forensic Dataset (Final)',
        'upload_type': 'dataset',
        'description': 'Final forensic audit of 42 sites. Atmospheric debt: ~8.5 MTCO2e.',
        'creators': [{'name': 'Kern-Cancan AI Division', 'affiliation': 'Kern County FMDZ'}]
    }
}
r = requests.post(BASE_URL, params=PARAMS, json=meta, headers=HEADERS)
if r.status_code != 201:
    print(f"❌ FAILED TO CREATE: {r.text}")
    exit()

dep_id = r.json()['id']
bucket_url = r.json()['links']['bucket']
print(f"✅ Created Deposition ID: {dep_id}")

# 3. UPLOAD WITH TIMEOUT PROTECTION
print(f"📤 Uploading {zip_name} (this may take a minute)...")
with open(zip_name, "rb") as fp:
    # Increased timeout for mobile network stability
    up = requests.put(f"{bucket_url}/{zip_name}", data=fp, params=PARAMS, timeout=300)

if up.status_code == 201 or up.status_code == 200:
    print("✅ Upload successful.")
else:
    print(f"❌ Upload failed: {up.text}")
    exit()

# 4. PUBLISH
print("🔏 Sealing the record (Publishing)...")
pub = requests.post(f"{BASE_URL}/{dep_id}/actions/publish", params=PARAMS)

if pub.status_code == 202:
    doi = pub.json().get('doi')
    print(f"\n🌟 SUCCESS! DATA IS PERMANENTLY INDEXED")
    print(f"🔗 DOI: {doi}")
    print(f"📍 URL: https://zenodo.org/record/{dep_id}")
    with open("zenodo_res.json", "w") as f:
        json.dump({"doi": doi, "id": dep_id}, f)
else:
    print(f"⚠️ Publish status: {pub.status_code}. Check dashboard: https://zenodo.org/deposit")
