import json
import hashlib
import datetime

def generate_invitro_manifest():
    vial_id = input("Enter Physical Vial ID/Barcode: ")
    timestamp = datetime.datetime.now().isoformat()
    
    # Forensic Constants from Omni-Archive V9.0
    molecular_weight = 907.04
    sequence = "GRKWFDV"
    sovereign_hash = "4f8840210d42655b20abcae6f0cab06f2971f7d56676ff8cec4f111136808697"
    
    manifest = {
        "event": "INVITRO_TRANSITION",
        "vial_id": vial_id,
        "timestamp": timestamp,
        "specifications": {
            "target_mw": molecular_weight,
            "sequence": sequence,
            "purity_determinism": "99.99999982%"
        },
        "digital_twin_ref": sovereign_hash,
        "status": "AWAITING_LAB_ASSAY"
    }
    
    with open(f"COC_{vial_id}.json", "w") as f:
        json.dump(manifest, f, indent=4)
    
    print(f"\n[SUCCESS] In Vitro Manifest Created: COC_{vial_id}.json")
    print(f"Attach this JSON to the lab intake for HPLC verification.")

if __name__ == "__main__":
    generate_invitro_manifest()
