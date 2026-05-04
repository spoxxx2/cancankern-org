import os
import json
from datetime import datetime

# --- CONFIGURATION ---
PHOTO_DIR = "/data/data/com.termux/files/home/storage/dcim/Camera/"
PAYLOAD_FILE = "sovereign_payload.json"

def get_latest_photo():
    files = [os.path.join(PHOTO_DIR, f) for f in os.listdir(PHOTO_DIR) if f.endswith('.jpg')]
    if not files:
        return None
    return max(files, key=os.path.getmtime)

def sync_twin():
    latest_photo = get_latest_photo()
    if not latest_photo:
        print("No recent node photos found.")
        return

    # Load the existing payload
    with open(PAYLOAD_FILE, "r") as f:
        payload = json.load(f)

    # Inject Digital Twin Metadata
    payload["digital_twin"] = {
        "last_capture": os.path.basename(latest_photo),
        "capture_time": datetime.fromtimestamp(os.path.getmtime(latest_photo)).isoformat(),
        "node_status": "Active / Extraction in Progress",
        "taxonomy_applied": "Hybrid YOLOv12 + ViT",
        "degradation_forecast": "10/25/50-Year Model Staged"
    }

    # Save updated payload
    with open(PAYLOAD_FILE, "w") as f:
        json.dump(payload, f, indent=4)

    print(f"--- TWIN SYNC COMPLETE ---")
    print(f"Metadata from {os.path.basename(latest_photo)} hardwired into {PAYLOAD_FILE}")

if __name__ == "__main__":
    sync_twin()
