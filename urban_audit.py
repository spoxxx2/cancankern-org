import json, os
from datetime import datetime

# BMC & Nuisance Abatement Configuration
def log_nuisance(item_type, condition, coordinates="35.3733, -119.0187"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    audit_id = f"SITE-{datetime.now().strftime('%m%d%H%M')}"
    
    report = {
        "audit_id": audit_id,
        "timestamp": ts,
        "location": coordinates,
        "category": "Urban Asset/Safety",
        "observations": {
            "type": item_type, # Graffiti, Pothole, Illegal Dumping
            "condition": condition,
            "compliance_ref": "BMC § 9.36.030 (Graffiti) / § 8.80 (Nuisance)"
        },
        "monetization": {
            "liability_surcharge": 15.00,
            "abatement_priority": "High" if "Fresh" in condition else "Medium"
        }
    }
    
    os.makedirs("audits/site_safety", exist_ok=True)
    with open(f"audits/site_safety/{audit_id}.json", "w") as f:
        json.dump(report, f, indent=4)
    
    print(f"🚨 {item_type} LOGGED: {condition} at {ts}")
    print(f"💰 Liability Surcharge Added: $15.00")

if __name__ == "__main__":
    # In practice, your Hybrid YOLOv12 model triggers this
    log_nuisance("Graffiti", "Fresh Paint - South Loading Dock")
