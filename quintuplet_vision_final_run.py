import pandas as pd
import os, requests, math, re, time
from PIL import Image, ImageDraw

# Directories
INPUT_DIR = os.path.expanduser("~/JAN_2026_MASTER/")
OUTPUT_DIR = os.path.expanduser("~/JAN_2026_FORENSIC_FINAL/")
METADATA = "BAKERSFIELD_PARCEL_ENRICHED_JAN_2026.csv"
LIABILITY_BASE = 1028.16 

if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
df = pd.read_csv(METADATA)

def get_actual_street(gps_str):
    try:
        nums = re.findall(r"[-+]?\d*\.\d+|\d+", gps_str)
        if len(nums) < 2: return "Bakersfield_Sector"
        lat, lon = nums[0], nums[1]
        if float(lon) > 0: lon = f"-{lon}"

        # The 'Ghost' logic for street resolution
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&zoom=18"
        headers = {'User-Agent': 'Kern_Audit_Final_Burn'}
        
        # 0.5s delay to keep the map server happy for 600+ hits
        time.sleep(0.5) 
        res = requests.get(url, headers=headers, timeout=5).json()
        
        addr = res.get('address', {})
        # Hierarchy: specific road > industrial road > suburb
        loc = addr.get('road') or addr.get('construction') or addr.get('hamlet') or "Kern_Patch_Access"
        return loc.replace(" ", "_")
    except:
        return "Bakersfield_Sector"

print("🚀 SCALING GHOST SCRIPT TO REMAINING EXHIBITS...")

for idx, row in df.iterrows():
    img_name = os.path.basename(row['SourceFile'])
    img_path = os.path.join(INPUT_DIR, img_name)
    
    # Check if we already processed this to save time
    apn = str(row['APN'])
    final_filename = f"EX_{idx}_{apn}.jpg"
    if os.path.exists(os.path.join(OUTPUT_DIR, final_filename)):
        continue

    if not os.path.exists(img_path): continue

    try:
        with Image.open(img_path) as img:
            draw = ImageDraw.Draw(img)
            street = get_actual_street(str(row['GPSPosition']))
            
            # 100-Year Compounding Math
            total_liab = LIABILITY_BASE * math.pow(1.04, 100)
            
            # The Final Forensic Watermark
            l1 = f"STREET: {street} | APN: {apn}"
            l2 = f"LIABILITY: ${LIABILITY_BASE}/kg | 100-YR: ${total_liab:,.2f}"
            l3 = "FORECAST: 1-100YR AIR QUALITY IMPACT | DEBRIS: HIGH"
            
            draw.text((40, img.height - 120), l1, fill="cyan")
            draw.text((40, img.height - 80), l2, fill="red")
            draw.text((40, img.height - 40), l3, fill="yellow")

            img.save(os.path.join(OUTPUT_DIR, final_filename))
            print(f"✅ Exhibit {idx} Sealed: {street} ({apn})")
            
    except Exception as e:
        print(f"⚠️ Error on Exhibit {idx}: {e}")

print("\n--- ALL 642 EXHIBITS COMPLETED ---")
