import os, hashlib, shutil, time
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from geopy.geocoders import Nominatim

SOURCE = "/storage/emulated/0/DCIM/Camera"
# Initialize geolocator for the Kern San Joaquin Valley Air Basin node
geolocator = Nominatim(user_agent="cancan_forensic_93307")

def get_decimal_from_dms(dms, ref):
    try:
        degrees = float(dms[0])
        minutes = float(dms[1]) / 60.0
        seconds = float(dms[2]) / 3600.0
        if ref in ['S', 'W']:
            return -(degrees + minutes + seconds)
        return degrees + minutes + seconds
    except: return None

def get_dynamic_address(path):
    try:
        img = Image.open(path)
        exif = img._getexif()
        if not exif: return "No_Exif"
        
        gps_info = {}
        for tag, value in exif.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_info[sub_decoded] = value[t]
        
        if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
            lat = get_decimal_from_dms(gps_info['GPSLatitude'], gps_info['GPSLatitudeRef'])
            lon = get_decimal_from_dms(gps_info['GPSLongitude'], gps_info['GPSLongitudeRef'])
            
            if lat and lon:
                # Reverse Geocode
                location = geolocator.reverse(f"{lat}, {lon}", timeout=10)
                if location and 'address' in location.raw:
                    addr = location.raw['address']
                    # Grab Street/Road or House Number
                    street = addr.get('road', addr.get('house_number', addr.get('suburb', 'Street_Unknown')))
                    return street.replace(" ", "_").replace("/", "-")
        return "Unknown_Loc"
    except:
        return "Error_Ext"

print("🛰️ Overlord Vision: Pulling dynamic addresses from EXIF...")
files = [f for f in os.listdir(SOURCE) if f.lower().endswith(('.jpg', '.jpeg'))]

count = 0
for f in files:
    old_path = os.path.join(SOURCE, f)
    
    # 1. Pull Address
    addr_name = get_dynamic_address(old_path)
    
    # 2. Get Timestamp
    mtime = os.path.getmtime(old_path)
    timestamp = datetime.fromtimestamp(mtime).strftime("%Y%m%d_%H%M%S")
    
    # 3. Create Unique Hash
    f_hash = hashlib.md5(f.encode()).hexdigest()[:6].upper()
    
    new_name = f"AUD_{addr_name}_{timestamp}_{f_hash}.jpg"
    new_path = os.path.join(SOURCE, new_name)
    
    if not f.startswith("AUD_"):
        print(f"📍 Mapped: {f} -> {new_name}")
        shutil.move(old_path, new_path)
        count += 1
        # Nominatim policy: 1 second per request to avoid IP ban
        time.sleep(1.1)

print(f"🏁 SUCCESS: {count} assets dynamically renamed.")
