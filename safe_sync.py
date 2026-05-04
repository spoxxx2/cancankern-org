import os, json, time
from azure.cosmos import CosmosClient

URL = os.environ.get('COSMOS_ENDPOINT')
KEY = os.environ.get('COSMOS_KEY')
DB = 'CANCAN_DB'
CONT = 'Audits'
LOCAL_DIR = os.path.expanduser('~/cancankern-org/audits/')

try:
    client = CosmosClient(URL, KEY)
    container = client.get_database_client(DB).get_container_client(CONT)
    
    files = sorted([f for f in os.listdir(LOCAL_DIR) if f.startswith('TWIN_')], reverse=True)[:10]

    print("🔑 Applying Master Keys for Portal Visibility...")

    for file in files:
        with open(os.path.join(LOCAL_DIR, file), 'r') as f:
            data = json.load(f)
            
            # --- THE "VISIBLE" SCHEMA ---
            data['id'] = data.get('id', file.replace('.json', ''))
            data['partitionKey'] = '93305'
            data['zipCode'] = '93305'
            data['city'] = 'Bakersfield'
            
            # Common portal filters - adding these forces them onto the map
            data['status'] = 'Published'
            data['isLive'] = True
            data['verified'] = True
            data['clientId'] = 'CANCAN_KERN' 
            data['siteId'] = 'PEARL_ST'
            data['compliance'] = 'BMC § 8.32.190'
            
            container.upsert_item(data)
            print(f"✅ Synced & Published: {file}")
            time.sleep(0.1)

    print("\n🚀 DONE. Refresh cancankern.org. If it's still blank, we'll check the logs.")
except Exception as e:
    print(f"❌ ERROR: {e}")
