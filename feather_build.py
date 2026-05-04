import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

output_path = "/sdcard/Documents/CANCAN_MASTER_AUDIT_V1.pdf"
img_dir = "/sdcard/Documents/CANCAN_AI_TRAINING_SET/images/"
summary_img = os.path.expanduser("~/SUMMARY_PAGE.jpg")

c = canvas.Canvas(output_path, pagesize=letter)

# Page 1: Summary
if os.path.exists(summary_img):
    c.drawImage(summary_img, 0, 0, width=612, height=792)
    c.showPage()

# Pages 2-281: Forensic Images
files = sorted([f for f in os.listdir(img_dir) if f.endswith('.jpg')])
print(f"Found {len(files)} images. Starting lean build...")

for filename in files:
    try:
        path = os.path.join(img_dir, filename)
        # Using reportlab's drawImage - much lighter than Magick
        c.drawImage(path, 50, 50, width=512, height=692, preserveAspectRatio=True)
        c.drawString(50, 30, f"CANCAN Forensic Twin: {filename}")
        c.showPage()
        print(f"Logged: {filename}")
    except Exception as e:
        print(f"Skipping {filename}: {e}")

c.save()
print(f"SUCCESS: PDF saved to {output_path}")
