import json
print("--- FINALIZING VIRTUAL 3RD-PARTY COA ---")
with open('divine_coa_final.json', 'r') as f:
    coa = json.load(f)
    print(f"CERTIFICATE {coa['certification_id']} LOCKED.")
    print(f"PURITY: {coa['purity']} | SYNC: {coa['molecular_weight_sync']}")
