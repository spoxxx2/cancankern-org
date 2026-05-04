import json
import os

# Create the directory
os.makedirs('nft_vault', exist_ok=True)

# Node 93307 Base Data
base_metadata = {
    "symbol": "CANCAN",
    "seller_fee_basis_points": 2500,
    "external_url": "https://doi.org/10.5281/zenodo.19590407",
    "creators": [{"address": "PENDING_SOVEREIGN_WALLET", "share": 100}]
}

for i in range(544, 554):
    metadata = {
        **base_metadata,
        "name": f"Singularity {i}: Kinetic Lock",
        "description": f"Verified peptide lattice stabilization at 1588 m/s. Node 93307.",
        "attributes": [
            {"trait_type": "Velocity", "value": "1588 m/s"},
            {"trait_type": "pI Lock", "value": "12.32"},
            {"trait_type": "Singularity", "value": str(i)},
            {"trait_type": "Compliance", "value": "BMC § 8.32.190"}
        ],
        "properties": {
            "files": [{"uri": f"forensic_{i}.png", "type": "image/png"}],
            "category": "image"
        }
    }
    with open(f"nft_vault/metadata_{i}.json", "w") as f:
        json.dump(metadata, f, indent=4)

print("SUCCESS: 10 Forensic Metadata Assets locked in ~/nft_vault")
