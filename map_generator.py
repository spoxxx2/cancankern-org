import folium
from folium.plugins import HeatMap
import json
import os

def generate_shield_map():
    audit_path = os.path.expanduser('~/audits')
    data = []
    
    # Ensure the directory exists
    if not os.path.exists(audit_path):
        print(f"[-] Error: {audit_path} not found.")
        return

    for file in os.listdir(audit_path):
        if file.endswith('.json'):
            with open(os.path.join(audit_path, file)) as f:
                try:
                    audit = json.load(f)
                    # Extract coordinates from your Digital Twin metadata
                    if 'coordinates' in audit:
                        data.append([audit['coordinates']['lat'], audit['coordinates']['lng']])
                except:
                    continue

    # Center map on Bakersfield (Pearl St. / Panama Lane area)
    m = folium.Map(location=[35.378, -118.998], zoom_start=14, tiles='cartodbpositron')
    
    if data:
        HeatMap(data).add_to(m)
    
    # Create the public folder if it doesn't exist
    os.makedirs(os.path.expanduser('~/cancankern-org/public'), exist_ok=True)
    
    save_path = os.path.expanduser('~/cancankern-org/public/shield.html')
    m.save(save_path)
    print(f"[+] Administrative Shield Map Generated at {save_path}")

if __name__ == "__main__":
    generate_shield_map()
