import os, json
from azure.storage.blob import BlobServiceClient

# CONFIGURE THESE
connect_str = "YOUR_CONNECTION_STRING_HERE"
container_name = "compliance-vault"
local_path = "audits/compliance_ready"

def sync():
    if not os.path.exists(local_path):
        print("Vault not found. Skipping sync.")
        return
    
    try:
        service_client = BlobServiceClient.from_connection_string(connect_str)
        # Create container if it doesn't exist
        container_client = service_client.get_container_client(container_name)
        
        for filename in os.listdir(local_path):
            if filename.endswith(".json") or filename == "vault_log.txt":
                blob_client = service_client.get_blob_client(container=container_name, blob=filename)
                with open(os.path.join(local_path, filename), "rb") as data:
                    blob_client.upload_blob(data, overwrite=True)
                print(f"☁️ Cloud Sync Success: {filename}")
    except Exception as e:
        print(f"⚠️ Sync Error: {e}")

if __name__ == "__main__":
    sync()
