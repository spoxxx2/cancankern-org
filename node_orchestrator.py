import os
import json
import shutil
from datetime import datetime

# --- CONFIGURATION ---
BASE_DIR = os.getcwd()
TIERS = {
    "compliance": "./03_CLIENT_REPORTS",
    "vault": "./vault/digital_twins",
    "config": "./vault/config",
    "infra": "./infra",
    "archive": "./vault/archive"
}

def setup_node():
    for path in TIERS.values():
        os.makedirs(path, exist_ok=True)

def index_and_clean():
    registry = []
    print("🚀 Starting Panama Lane Node Orchestration...")

    for root, dirs, files in os.walk(BASE_DIR):
        # Prevent recursion into the vault during the scan
        if "vault" in root or ".git" in root or ".terraform" in root:
            continue

        for name in files:
            file_path = os.path.join(root, name)
            
            # 1. CATEGORIZE & ORGANIZE (Moving files to tiers)
            target_path = None
            
            # System & Config Files
            if name.endswith((".json", ".rules")) and name not in ["ZENITH_REGISTRY.json", "gemini.md"]:
                if "AIR_IMPACT" in name or "audit" in name:
                    target_path = os.path.join(TIERS["compliance"], name)
                elif any(x in name for x in ["firebase", "vercel", "project", "zenodo"]):
                    target_path = os.path.join(TIERS["config"], name)
            
            # Move the file if a target was identified
            if target_path and file_path != target_path:
                shutil.move(file_path, target_path)
                file_path = target_path # Update path for indexing

            # 2. INDEXING
            registry.append({
                "filename": name,
                "path": os.path.relpath(file_path),
                "timestamp": datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat(),
                "node": "Panama Lane 93307",
                "compliance_ref": "BMC § 8.32.190"
            })

    # Save the Global Registry
    with open("ZENITH_REGISTRY.json", "w") as f:
        json.dump(registry, f, indent=4)
    
    print(f"✅ Clean complete. {len(registry)} files indexed in ZENITH_REGISTRY.json")

if __name__ == "__main__":
    setup_node()
    index_and_clean()
