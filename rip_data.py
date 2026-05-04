import re
import glob

print(f"{'FILE':<20} | {'BRAND':<15} | {'CMC':<15} | {'WEIGHT'}")
print("-" * 65)

for f_path in glob.glob('audits/*.json'):
    try:
        with open(f_path, 'r') as f:
            content = f.read()
            
            # Use Regex to find the data regardless of JSON structure
            brand_match = re.search(r'"detected_brand":\s*"([^"]+)"', content)
            cmc_match = re.search(r'"sb54_covered_material":\s*"([^"]+)"', content)
            weight_match = re.search(r'"weight":\s*([\d.]+)', content)
            
            brand = brand_match.group(1) if brand_match else "Unknown"
            cmc = cmc_match.group(1) if cmc_match else "N/A"
            weight = weight_match.group(1) if weight_match else "0"
            
            if brand != "Unknown" or cmc != "N/A":
                print(f"{f_path:<20} | {brand:<15} | {cmc:<15} | {weight}kg")
            else:
                # If we still find nothing, it's likely a truly empty capture
                pass
    except Exception:
        continue
