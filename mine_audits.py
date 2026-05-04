import json
import glob
import os

print(f"{'FILE':<20} | {'BRAND':<15} | {'CMC':<15} | {'WEIGHT'}")
print("-" * 65)

# Scans your audits folder
for f_path in glob.glob('audits/*.json'):
    if os.path.getsize(f_path) == 0:
        print(f"{f_path:<20} | SKIPPING (Empty File)")
        continue
        
    try:
        with open(f_path, 'r') as f:
            d = json.load(f)
            # Reach into the nested metadata
            brand = d.get('brand_intelligence', {}).get('detected_brand', 'Unknown')
            # Handle both old and new metadata paths for SB 54
            cmc = d.get('compliance_metrics', {}).get('sb54_covered_material', 'N/A')
            weight = d.get('weight', 0)
            
            print(f"{f_path:<20} | {brand:<15} | {cmc:<15} | {weight}kg")
    except Exception as e:
        print(f"{f_path:<20} | ERROR: (Malformed JSON)")

