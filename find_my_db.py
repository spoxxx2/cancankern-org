import os
from azure.cosmos import CosmosClient

# Using the confirmed 8883 endpoint from your env
URL = os.environ.get('COSMOS_ENDPOINT')
KEY = os.environ.get('COSMOS_KEY')

try:
    client = CosmosClient(URL, credential=KEY)
    print("\n🔍 SCANNING AZURE ACCOUNT: 8883")
    print("-" * 30)
    
    databases = list(client.list_databases())
    if not databases:
        print("❌ No databases found in this account.")
    else:
        for db in databases:
            print(f"✅ DATABASE FOUND: {db['id']}")
            database = client.get_database_client(db['id'])
            containers = list(database.list_containers())
            for container in containers:
                print(f"   ∟ 📦 CONTAINER FOUND: {container['id']}")
    print("-" * 30)
except Exception as e:
    print(f"❌ ERROR: {e}")
