import json
import os

def check_vault(path):
    print(f"\n--- AUDITING: {path} ---")
    files = [f for f in os.listdir(path) if f.endswith('.json')]
    valid_count = 0
    for f_name in files:
        full_path = os.path.join(path, f_name)
        try:
            with open(full_path, 'r') as f:
                data = json.load(f)
                # Verify DOI Anchor
                if "DOI" not in str(data):
                    print(f" [!] MISSING DOI: {f_name}")
                else:
                    valid_count += 1
        except Exception as e:
            print(f" [X] CORRUPT FILE: {f_name} | Error: {e}")
    print(f"RESULT: {valid_count}/{len(files)} files verified and healthy.")

# Audit both the Black Swan and Anomaly vaults
check_vault('/data/data/com.termux/files/home/miracle_vault')
check_vault('/data/data/com.termux/files/home/anomaly_vault')
