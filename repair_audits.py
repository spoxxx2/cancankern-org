import json
import glob
import re
import os

def fix_json_content(content):
    # 1. Remove trailing commas before a closing bracket or brace
    content = re.sub(r',\s*([\]}])', r'\1', content)
    # 2. Try to close unclosed objects/arrays if they end abruptly
    content = content.strip()
    if not content.endswith('}'):
        content += '}'
    return content

audit_files = glob.glob('audits/*.json')
print(f"Attempting repair on {len(audit_files)} files...")

for f_path in audit_files:
    try:
        with open(f_path, 'r+') as f:
            raw = f.read()
            if not raw.strip(): continue # Skip truly empty files
            
            try:
                json.loads(raw) # Check if already valid
            except json.JSONDecodeError:
                fixed = fix_json_content(raw)
                try:
                    json.loads(fixed)
                    f.seek(0)
                    f.write(fixed)
                    f.truncate()
                    print(f"REPAIRED: {f_path}")
                except:
                    print(f"STILL BROKEN: {f_path} - Manual check required.")
    except Exception as e:
        print(f"FAILED TO ACCESS: {f_path}")
