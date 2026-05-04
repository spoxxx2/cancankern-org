import os
import json
from azure.cosmos import CosmosClient

# --- CONFIG (Sync with your push_verified.py) ---
URL = os.environ.get('COSMOS_URL')
KEY = os.environ.get('COSMOS_KEY')
DATABASE_NAME = 'cancan-db'
CONTAINER_NAME = 'audits'

def check_live_audits():
    try:
        client = CosmosClient(URL, credential=KEY)
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client(CONTAINER_NAME)

        print("[*] Fetching live audits from cancankern.org database...")
        # Querying for the last 10 entries
        query = "SELECT TOP 10 c.id, c.vit_confidence, c.timestamp FROM c ORDER BY c._ts DESC"
        items = list(container.query_items(query=query, enable_cross_partition_query=True))

        if not items:
            print("⚪ No audits found on the website yet.")
        else:
            print(f"✅ Found {len(items)} live audits:\n")
            print(f"{'AUDIT ID':<40} | {'CONFIDENCE':<10}")
            print("-" * 55)
            for item in items:
                print(f"{item.get('id'):<40} | {item.get('vit_confidence', 'N/A'):<10}")
    except Exception as e:
        print(f"❌ Error connecting to Azure: {e}")

if __name__ == "__main__":
    check_live_audits()
