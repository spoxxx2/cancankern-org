import os, requests, sys

def vault_file(file_path):
    # This uses your permanent Refresh Token (generated once)
    refresh_token = os.getenv('ONEDRIVE_REFRESH_TOKEN')
    client_id = "000000004c12ae29" # MS Public Client ID
    
    # 1. Get a fresh Access Token
    token_url = "https://login.live.com/oauth20_token.srf"
    data = {"client_id": client_id, "refresh_token": refresh_token, "grant_type": "refresh_token"}
    access_token = requests.post(token_url, data=data).json().get('access_token')
    
    # 2. Upload with Address Metadata
    file_name = os.path.basename(file_path)
    upload_url = f"https://graph.microsoft.com/v1.0/me/drive/root:/CANCAN_Vault/{file_name}:/content"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    with open(file_path, 'rb') as f:
        requests.put(upload_url, headers=headers, data=f)
    print(f"Vaulted: {file_name}")

if __name__ == "__main__":
    vault_file(sys.argv[1])
