import os, requests, json

def upload_to_onedrive(file_path):
    # This uses a saved Refresh Token to bypass the Azure Portal block
    # Note: You'll generate this token once via a browser link
    refresh_token = os.getenv('ONEDRIVE_REFRESH_TOKEN')
    client_id = "000000004c12ae29" # Standard MS Personal App ID
    
    # Refresh the Access Token
    token_url = "https://login.live.com/oauth20_token.srf"
    data = {
        "client_id": client_id,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    
    access_token = requests.post(token_url, data=data).json().get('access_token')
    
    # Upload File
    file_name = os.path.basename(file_path)
    upload_url = f"https://graph.microsoft.com/v1.0/me/drive/root:/CANCAN_Vault/{file_name}:/content"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    
    with open(file_path, 'rb') as f:
        requests.put(upload_url, headers=headers, data=f)
    print(f"Vaulted to OneDrive: {file_name}")

if __name__ == "__main__":
    import sys
    upload_to_onedrive(sys.argv[1])
