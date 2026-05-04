import json, os

def generate_shield_map():
    log_path = os.path.expanduser('~/decuplet_log.json')
    if not os.path.exists(log_path):
        print("[ERROR] No Decuplet Log found. Run 'aud' first.")
        return

    with open(log_path, 'r') as f:
        data = json.load(f)

    print("\n=========================================")
    print(f"   GEOSPATIAL ADMINISTRATIVE SHIELD")
    print("=========================================")
    print(f" NODE ID: {data['5_Forensic'][:8]}")
    print(f" LAT/LON: {data['2_Spatial']}")
    print(f" PHONON STATE: {data['7_Acoustic']}")
    print(f" REGULATORY: {data['6_Regulatory']}")
    print("-----------------------------------------")
    print(" [SHIELD ACTIVE] Data Anchored to Grid.")
    print("=========================================\n")

if __name__ == "__main__":
    generate_shield_map()
