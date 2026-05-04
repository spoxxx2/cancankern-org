import os
import json
from azure.cosmos import CosmosClient

# --- HARDWIRED TO 8883 NODE ---
URL = os.environ.get('COSMOS_ENDPOINT')
KEY = os.environ.get('COSMOS_KEY')
DATABASE_NAME = 'CANCAN_DB'
CONTAINER_NAME = 'Audits'
LOCAL_DIR = "/data/data/com.termux/files/home/Forensic_Audits"

def sync_production():
    try:
        client = CosmosClient(URL, credential=KEY)
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client(CONTAINER_NAME)

        print(f"[*] Uplink Active: {DATABASE_NAME} -> {CONTAINER_NAME}")
        
        synced_count = 0
        for file in os.listdir(LOCAL_DIR):
            if file.endswith(".json"):
                with open(os.path.join(LOCAL_DIR, file), 'r') as f:
                    data = json.load(f)
                    # Ensuring the Partition Key is set for the 93305 filter
                    # If your container uses a different PK name, we'll see it here
                    data['partitionKey'] = "93305" 
                    container.upsert_item(data)
                synced_count += 1
                print(f"✅ Synced: {file}")

        if synced_count > 0:
            print(f"\n🚀 SUCCESS: {synced_count} audits sent to cancankern.org")
        else:
            print("⚠️ No new JSON audits found in Forensic_Audits folder.")

    except Exception as e:
        print(f"❌ UPLINK ERROR: {e}")

if __name__ == "__main__":
    sync_production()
