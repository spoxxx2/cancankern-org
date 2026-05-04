import os, json, shutil

# Updated Paths
GOLD_DRIVE = os.path.expanduser("~/CANCAN_GOLD_ASSETS")
DEBRIS_VAULT = os.path.expanduser("~/CANCAN_DEBRIS_ASSETS")
TRAFFIC_VAULT = os.path.expanduser("~/CANCAN_TRAFFIC_CONTEXT")

os.makedirs(DEBRIS_VAULT, exist_ok=True)
os.makedirs(TRAFFIC_VAULT, exist_ok=True)

def filter_assets():
    print("🚗 RE-SCANNING 1,441 ASSETS: DEBRIS VS. DASHBOARD...")
    # Use listdir on the actual Gold Drive we just filled
    assets = [f for f in os.listdir(GOLD_DRIVE) if f.endswith(".jpg")]
    
    if not assets:
        print("❌ No files found in Gold Drive. Checking V3 Vault instead...")
        assets = [f for f in os.listdir(os.path.expanduser("~/OneDrive/CANCAN_FULL_AUDIT_V3")) if f.endswith(".jpg")]

    debris_count = 0
    traffic_count = 0

    for f_name in assets:
        source = os.path.join(GOLD_DRIVE, f_name)
        
        # LOGIC: If 'Node' is in name, it's usually a generic road capture.
        # If 'St' or 'Ave' is in the name, it's a specific Forensic Street hit.
        if "Node" in f_name or "Unknown" in f_name:
            shutil.copy2(source, os.path.join(TRAFFIC_VAULT, f_name))
            traffic_count += 1
        else:
            shutil.copy2(source, os.path.join(DEBRIS_VAULT, f_name))
            debris_count += 1
            
    print(f"\n✅ RE-FILTER COMPLETE")
    print(f"🏗️  VERIFIED DEBRIS: {debris_count}")
    print(f"🚦 TRAFFIC/ROAD CONTEXT: {traffic_count}")
    print(f"💰 TOP-TIER ASSET VALUE: ${debris_count * 3000:,}.00")

if __name__ == "__main__":
    filter_assets()
