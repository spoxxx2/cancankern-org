import os
from azure.cosmos import CosmosClient

URL = os.environ.get('COSMOS_ENDPOINT')
KEY = os.environ.get('COSMOS_KEY')

client = CosmosClient(URL, credential=KEY)

print("[*] Databases in this account:")
for db in client.list_databases():
    print(f" -> Database ID: {db['id']}")
    database = client.get_database_client(db['id'])
    for container in database.list_containers():
        print(f"    - Container ID: {container['id']}")
