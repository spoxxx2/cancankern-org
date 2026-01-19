import os
import subprocess
from vision_core import process_image

def quick_capture():
    print("📸 Initializing Quick Capture...")
    # Finds the most recent JPG in your Camera folder
    cmd = "ls -t ~/storage/dcim/Camera/*.jpg 2>/dev/null | head -1"
    last_photo = subprocess.getoutput(cmd)
    
    if not last_photo or "ls:" in last_photo:
        print("❌ No photo found. Run 'termux-setup-storage' and take a picture first!")
        return

    print(f"🔍 Analyzing: {os.path.basename(last_photo)}")
    process_image(last_photo)
    print("✅ Audit Complete.")

if __name__ == "__main__":
    quick_capture()
