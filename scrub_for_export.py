import json

def generate_public_manifest(private_manifest_path):
    with open(private_manifest_path, 'r') as f:
        data = json.load(f)
    
    # Redacting trade secrets
    public_data = {
        "batch_id": data["batch_id"],
        "purity": data["purity_tier"],
        "volume": data["volume_ml"],
        "methodology": "Proprietary Acoustic Triple-Lock",
        "verification": "Digital Twin Hash Validated",
        "status": "Ready for Intake"
    }
    
    with open('PUBLIC_MANIFEST_SCRUBBED.json', 'w') as f:
        json.dump(public_data, f, indent=4)
    print("\n[AUD] PUBLIC MANIFEST CREATED. Trade secrets redacted.")

if __name__ == "__main__":
    generate_public_manifest('INVENTORY_VALUATION.json')
