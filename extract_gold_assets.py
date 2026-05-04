import os, json, shutil

# Paths
VAULT_V3 = os.path.expanduser("~/OneDrive/CANCAN_FULL_AUDIT_V3")
GOLD_DRIVE = os.path.expanduser("~/CANCAN_GOLD_ASSETS")
os.makedirs(GOLD_DRIVE, exist_ok=True)

def extract():
    print("🚚 EXTRACTING 479 GOLDEN ASSETS TO LOCAL DRIVE...")
    json_files = [f for f in os.listdir(VAULT_V3) if f.endswith(".json")]
    
    count = 0
    for f_name in json_files:
        with open(os.path.join(VAULT_V3, f_name), 'r') as f:
            data = json.load(f)
        
        # Get the original source path and the newly resolved street name
        source_img = data.get("source")
        street = data.get("street_name", "Bakersfield_Node").replace(" ", "_")
        f_hash = data.get("hash", "no_hash")[:8]
        
        if source_img and os.path.exists(source_img):
            # Create a clean, driveable name: 93305_Inyo_St_a1b2c3d4.jpg
            new_name = f"{street}_{f_hash}.jpg"
            target_path = os.path.join(GOLD_DRIVE, new_name)
            
            shutil.copy2(source_img, target_path)
            count += 1
            if count % 50 == 0:
                print(f"📦 {count}/479 assets moved to Gold Drive...")

    print(f"\n💎 SUCCESS: {count} Physical Assets are now in {GOLD_DRIVE}")
    print(f"📂 You can now 'cd ~/CANCAN_GOLD_ASSETS' to see your work.")

if __name__ == "__main__":
    extract()
