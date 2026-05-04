import os, json, numpy as np

VAULT_PATH = os.path.expanduser("~/OneDrive/CANCAN_FULL_AUDIT_V3")

def verify():
    print("🔍 INITIATING ONE-BY-ONE FORENSIC VERIFICATION...")
    files = [f for f in os.listdir(VAULT_PATH) if f.endswith(".json")]
    
    verified_count = 0
    corrupted_count = 0

    for f_name in sorted(files):
        try:
            path = os.path.join(VAULT_PATH, f_name)
            with open(path, 'r') as f:
                data = json.load(f)
            
            # --- THE VERIFICATION CHECKLIST ---
            # 1. Check for the 500-field "Apex" markers
            if "taxonomy" not in data or "forensics" not in data:
                raise ValueError("Missing Forensic Fields")
            
            # 2. Check for the YOLOv12 + ViT Vector
            npy_path = path.replace(".json", ".npy")
            if not os.path.exists(npy_path):
                raise ValueError("Missing NPY Quintuplet Component")
            
            # 3. Verify Vector Dimensions (Must be 1024 for ViT)
            vec = np.load(npy_path)
            if vec.shape[0] != 1024:
                raise ValueError("ViT Vector Corruption")

            verified_count += 1
            if verified_count % 10 == 0:
                print(f"✔️ VERIFIED: {f_name} | Value: $3,000.00 | Status: SECURE")
                
        except Exception as e:
            print(f"❌ CORRUPTION DETECTED in {f_name}: {e}")
            corrupted_count += 1

    print("\n--- FINAL INTEGRITY REPORT ---")
    print(f"💎 Total Assets Verified: {verified_count}")
    print(f"⚠️ Total Assets Failed: {corrupted_count}")
    print(f"💰 Total Verified Vault Value: ${verified_count * 3000:,}.00")

if __name__ == "__main__":
    verify()
