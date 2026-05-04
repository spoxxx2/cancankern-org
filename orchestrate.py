import os
import json
import shutil
from datetime import datetime

# 1. DEFINE TIERS & METADATA
TIERS = {
    "compliance": "./03_CLIENT_REPORTS",
    "vault_active": "./vault/active",
    "system_config": "./vault/config"
}

def get_forecast(filename, material="Unclassified"):
    """Generates a 10/25/50-year debris degradation forecast metadata."""
    # Logic based on BMC § 8.32.190 compliance
    forecasts = {
        "Ferrous Metal": {"10y": "Significant Oxidation", "25y": "Structural Fragmentation", "50y": "Complete Mineralization"},
        "Polymer": {"10y": "Microplastic Shedding", "25y": "Brittle/Yellowing", "50y": "Partial Photo-degradation"},
        "Unclassified": {"10y": "Unknown", "25y": "Unknown", "50y": "Unknown"}
    }
    return forecasts.get(material, forecasts["Unclassified"])

def generate_and_sync():
    setup_node()
    registry = []
    
    for root, _, files in os.walk("."):
        if any(x in root for x in [".git", ".terraform"]): continue
        for f in files:
            path = os.path.join(root, f)
            # Determine material from filename or default
            material = "Ferrous Metal" if "ferrous" in f.lower() else "Unclassified"
            
            registry.append({
                "file": f,
                "location": path,
                "material_taxonomy": material,
                "50y_forecast": get_forecast(f, material),
                "timestamp": datetime.now().isoformat()
            })
    
    # Save Locally
    with open("ZENITH_REGISTRY.json", "w") as f:
        json.dump(registry, f, indent=4)
    
    # SYNC TO DRIVE (Requires rclone or gdrive CLI configured on node)
    # If rclone is not installed, this will log the intent.
    print("✓ ZENITH_REGISTRY.json saved locally.")
    os.system("rclone copy ZENITH_REGISTRY.json gdrive:/Audits/Registry/ 2>/dev/null || echo '! Drive Sync: Configure rclone to automate cloud backup.'")

def setup_node():
    for path in TIERS.values():
        os.makedirs(path, exist_ok=True)

if __name__ == "__main__":
    generate_and_sync()
