import os, hashlib, zipfile, shutil
from PIL import Image

# Overlord Pathing - Targets based on your 'find' results
TARGET_DIR = "/storage/emulated/0/DCIM/Camera"
TEMP_EXTRACT = os.path.expanduser("~/audit_depot")

# Direct paths where your ZIPs live
SEARCH_PATHS = [
    "/storage/emulated/0/Download",
    "/storage/emulated/0/CANCAN_BACKUP",
    "/storage/emulated/0/CANCAN_DATASETS"
]

os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(TEMP_EXTRACT, exist_ok=True)

def get_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def is_real_photo(file_path):
    """Filters out icons and small thumbnails to keep only audit-grade images"""
    try:
        with Image.open(file_path) as img:
            if img.format == "PNG": return False 
            # Real audit photos are usually > 300KB
            if os.path.getsize(file_path) > 300000:
                return True
        return False
    except: return False

moved = 0
seen_hashes = set()

print("🛰️ Overlord Vision: Processing Remote ZIP Clusters...")

for folder in SEARCH_PATHS:
    if not os.path.exists(folder): continue
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(".zip"):
                zip_path = os.path.join(root, f)
                print(f"📦 Extracting: {f}")
                try:
                    with zipfile.ZipFile(zip_path, 'r') as z:
                        z.extractall(TEMP_EXTRACT)
                        
                        # Process images from this specific ZIP
                        for e_root, _, e_files in os.walk(TEMP_EXTRACT):
                            for img_f in e_files:
                                if img_f.lower().endswith(('.jpg', '.jpeg', '.heic')):
                                    src = os.path.join(e_root, img_f)
                                    f_hash = get_hash(src)
                                    if f_hash not in seen_hashes and is_real_photo(src):
                                        seen_hashes.add(f_hash)
                                        shutil.move(src, os.path.join(TARGET_DIR, f"AUDIT_TRAIN_{moved}_{img_f}"))
                                        moved += 1
                    # Clear temp after each ZIP to preserve space
                    shutil.rmtree(TEMP_EXTRACT)
                    os.makedirs(TEMP_EXTRACT)
                except Exception as e:
                    print(f"⚠️ Error in {f}: {e}")

shutil.rmtree(TEMP_EXTRACT, ignore_errors=True)
print(f"✅ OVERLORD SUCCESS: {moved} real photos moved to {TARGET_DIR}.")
