import json
import glob
import re
import os

def sentinel_repair(content):
    content = content.strip()
    if not content: return None
    # Fix unclosed braces from truncated logs
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces > close_braces:
        content += '}' * (open_braces - close_braces)
    # Strip trailing commas that break strict JSON parsing
    content = re.sub(r',\s*([\]}])', r'\1', content)
    return content

audit_files = glob.glob('audits/*.json')
repaired_count = 0

print("--- Sentinel Deep Repair Initialized ---")

for f_path in audit_files:
    try:
        if os.path.getsize(f_path) == 0:
            continue
            
        with open(f_path, 'r') as f:
            raw = f.read()
        
        repaired_json = sentinel_repair(raw)
        if not repaired_json:
            continue
            
        try:
            data = json.loads(repaired_json)
            # Write the clean version back
            with open(f_path, 'w') as f:
                json.dump(data, f, indent=4)
            
            brand = data.get('brand_intelligence', {}).get('detected_brand', 'Unknown')
            if brand != 'Unknown':
                print(f"RECOVERED: {f_path} | Brand: {brand}")
                repaired_count += 1
        except json.JSONDecodeError:
            continue
    except Exception:
        continue

print(f"--- Repair Cycle Complete: {repaired_count} Files Saved ---")
