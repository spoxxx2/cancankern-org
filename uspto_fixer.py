import os
import re
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def sanitize_filename(filename):
    # USPTO rule: No underscores at start, no brackets/commas, max 100 chars
    clean_name = re.sub(r'[^A-Za-z0-9_\-]', '', filename.replace(" ", "_"))
    if clean_name.startswith(('_', '-')):
        clean_name = "file_" + clean_name
    return clean_name[:96] + ".pdf"

def convert_to_uspto_pdf(input_path, output_folder):
    # Load Image
    img = Image.open(input_path)
    img_width, img_height = img.size
    
    # USPTO Letter size: 8.5 x 11 inches (612 x 792 points)
    page_w, page_h = letter
    
    # Define USPTO Margins (in points: 1 inch = 72 pts)
    # Top: 1", Left: 1", Right: 0.6", Bottom: 0.4"
    margin_left = 72
    margin_top = 72
    usable_w = page_w - (72 + 43) # Left + Right
    usable_h = page_h - (72 + 28) # Top + Bottom
    
    # Calculate Scaling to fit "Sight Area"
    ratio = min(usable_w / img_width, usable_h / img_height)
    new_w, new_h = img_width * ratio, img_height * ratio
    
    # Save to output
    out_name = sanitize_filename(os.path.basename(input_path))
    c = canvas.Canvas(os.path.join(output_folder, out_name), pagesize=letter)
    
    # Position image (centered in usable area)
    x_offset = margin_left + (usable_w - new_w) / 2
    y_offset = (page_h - margin_top) - new_h
    
    c.drawInlineImage(img, x_offset, y_offset, width=new_w, height=new_h)
    c.showPage()
    c.save()
    print(f"✅ Success: {out_name} generated.")

# Example Usage for Panama Lane Node drawings
# convert_to_uspto_pdf("draft_drawing_01.png", "./uspto_upload_ready")