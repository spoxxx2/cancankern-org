import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Node-specific paths
SCREENSHOT_DIR = "/sdcard/DCIM/Screenshots"
LOG_FILE = os.path.expanduser("~/digital_twin_manifest.json")

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(('.png', '.jpg')):
            return
        print(f"[*] New Screenshot Detected: {event.src_path}")
        self.process_audit(event.src_path)

    def process_audit(self, path):
        # Trigger your existing vision_master logic
        os.system(f"python ~/vision_master.py --input {path} --mode forensic")
        
        entry = {
            "timestamp": time.ctime(),
            "file": os.path.basename(path),
            "node": "Panama_Lane_93307",
            "compliance": "BMC § 8.32.190"
        }
        
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[+] Digital Twin Logged: {os.path.basename(path)}")

if __name__ == "__main__":
    if not os.path.exists(SCREENSHOT_DIR):
        print(f"[!] Error: {SCREENSHOT_DIR} not found. Check Termux storage permissions.")
    else:
        observer = Observer()
        observer.schedule(ScreenshotHandler(), SCREENSHOT_DIR, recursive=False)
        observer.start()
        print("[>] Screenshot Watcher Active. Standing by...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
