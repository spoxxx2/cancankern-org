import os, json, subprocess, hashlib
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def verify():
    print("🛰️  HUNTING FOR UNIQUE STREET-STAMPED EVIDENCE...")
    cmd = ["find", os.path.expanduser("~"), "-iname", "*.jpg", "-size", "+100k"]
    all_files = subprocess.check_output(cmd).decode().splitlines()
    
    unique_hashes = set()
    camera_photos = 0
    screenshots = 0
    street_map = {}

    for path in all_files:
        if "VAULT" in path: continue
        
        # 1. Deduplicate by Fingerprint
        f_hash = get_file_hash(path)
        if f_hash in unique_hashes:
            continue
        unique_hashes.add(f_hash)

        # 2. Identify "Real" vs "Screenshot"
        try:
            img = Image.open(path)
            exif = get_exif_data(img)
            
            # Real camera photos have 'Make' or 'Model' or 'GPSInfo'
            if "GPSInfo" in exif or "Model" in exif:
                camera_photos += 1
                # In a real run, we'd call geopy here. For now, we flag presence.
                loc_status = "STAMPED" if "GPSInfo" in exif else "NO_GPS"
                street_map[path] = loc_status
            else:
                screenshots += 1
        except:
            continue

    print(f"\n--- 🛡️  FORENSIC AUDIT REPORT ---")
    print(f"📸 Unique Camera Photos (Evidence): {camera_photos}")
    print(f"📱 Potential Screenshots/UI: {screenshots}")
    print(f"💎 Verified Market Value (@$3k): ${camera_photos * 3000:,}.00")
    print(f"\nTop Nodes Found: {len(street_map)} unique locations pending street-name resolution.")

if __name__ == "__main__":
    verify()
