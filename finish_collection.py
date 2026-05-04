import json
import os

os.makedirs('miracle_vault', exist_ok=True)

# Generate the remaining 90 pieces (11 to 100)
for i in range(11, 101):
    metadata = {
        "name": f"Node 1501-P: Black Swan {i}/100",
        "symbol": "CANCAN",
        "description": "10B Run Event Horizon Miracle. Verified 1588 m/s sync. Node 93307.",
        "seller_fee_basis_points": 2500,
        "attributes": [
            {"trait_type": "Sim_Volume", "value": "10,000,000,000"},
            {"trait_type": "Probability", "value": "Black Swan (1e-10)"},
            {"trait_type": "Constant", "value": "1588 m/s"},
            {"trait_type": "Set_Index", "value": f"{i}/100"}
        ],
        "properties": {
            "files": [{"uri": f"miracle_{i}.png", "type": "image/png"}],
            "category": "image"
        }
    }
    with open(f"miracle_vault/miracle_{i}.json", "w") as f:
        json.dump(metadata, f, indent=4)
print("SUCCESS: Full set of 100 Metadata JSONs now locked in ~/miracle_vault")
