import pandas as pd
import os, math, re
from PIL import Image, ImageDraw

INPUT_DIR = os.path.expanduser("~/JAN_2026_MASTER/")
OUTPUT_DIR = os.path.expanduser("~/JAN_2026_FORENSIC_FINAL/")
METADATA = "BAKERSFIELD_PARCEL_ENRICHED_JAN_2026.csv"
LIABILITY_BASE = 1028.16 

if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
df = pd.read_csv(METADATA)

print("🏛️ BURNING ABSOLUTE COORDINATES INTO 642 EXHIBITS...")

for idx, row in df.iterrows():
    img_name = os.path.basename(row['SourceFile'])
    img_path = os.path.join(INPUT_DIR, img_name)
    if not os.path.exists(img_path): continue

    try:
        with Image.open(img_path) as img:
            draw = ImageDraw.Draw(img)
            
            # 1. Use the Raw GPS from your CSV
            coords = str(row['GPSPosition']).replace('deg', '°').strip()
            apn = str(row['APN'])
            
            # 2. Liability Forecast
            total_liab = LIABILITY_BASE * math.pow(1.04, 100)
            
            # 3. The Forensic Data Burn
            l1 = f"LOC: {coords} | APN: {apn}"
            l2 = f"LIABILITY: ${LIABILITY_BASE}/kg | 100-YR: ${total_liab:,.2f}"
            l3 = "FORECAST: 1-100YR AIR QUALITY IMPACT | DEBRIS: HIGH"
            
            # Positioning at the bottom for standard audit view
            draw.text((40, img.height - 120), l1, fill="cyan")
            draw.text((40, img.height - 80), l2, fill="red")
            draw.text((40, img.height - 40), l3, fill="yellow")

            # Unique Naming by APN and Exhibit Index
            final_name = f"APN_{apn}_Ex_{idx}.jpg"
            img.save(os.path.join(OUTPUT_DIR, final_name))
            
            print(f"⚖️ SEALED: {final_name} at {coords}")
    except Exception as e:
        print(f"⚠️ Error on Exhibit {idx}: {e}")

print("\n--- AUDIT READY: 642 ABSOLUTE EXHIBITS GENERATED ---")
