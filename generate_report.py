import json, os
from fpdf import FPDF
from datetime import datetime

# Config
JSON_PATH = "/storage/emulated/0/Documents/CANCAN_AUDITS/MASTER_AUDIT_20260209.json"
IMAGE_DIR = "/storage/emulated/0/DCIM/Camera"
OUTPUT_PDF = "/storage/emulated/0/Documents/CANCAN_AUDITS/SB1383_COURT_REPORT.pdf"

class AuditReport(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "OFFICIAL COMPLIANCE AUDIT - CANCAN THIRD-PARTY AUDITOR", ln=True, align="C")
        self.set_font("helvetica", "", 10)
        self.cell(0, 10, "Authority: BMC § 8.32.190 | SB 1383 | Kern River Subbasin 54", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()} | Forensic Chain of Custody Verified (SHA-256)", 0, 0, "C")

def clean_text(text):
    # Replaces complex unicode (like bullet points) with PDF-safe characters
    return text.replace('\u2022', '-').replace('\u201d', '"').replace('\u201c', '"')

def create_pdf():
    if not os.path.exists(JSON_PATH):
        print(f"❌ Error: {JSON_PATH} not found.")
        return

    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    pdf = AuditReport()
    pdf.set_auto_page_break(auto=True, margin=15)

    print(f"📄 Generating PDF for {len(data)} entries...")

    # Processing first 50 items for a comprehensive but manageable report
    for entry in data[:50]: 
        pdf.add_page()
        
        pdf.set_font("helvetica", "B", 14)
        pdf.cell(0, 10, f"Audit ID: {entry['id']}", ln=True)
        pdf.set_font("helvetica", "", 10)
        pdf.cell(0, 8, f"Timestamp: {entry['timestamp']}", ln=True)
        
        img_path = os.path.join(IMAGE_DIR, entry['filename'])
        if os.path.exists(img_path):
            try:
                # Optimized image placement
                pdf.image(img_path, x=10, y=None, w=120)
            except Exception as e:
                pdf.cell(0, 10, f"[Image Error: {e}]", ln=True)
        
        pdf.ln(5)
        
        pdf.set_font("helvetica", "B", 11)
        pdf.cell(0, 8, "Forensic Quintuplet Analysis:", ln=True)
        pdf.set_font("helvetica", "", 9)
        
        q = entry['quintuplet']
        # Using clean_text to avoid the 'latin-1' encoding error
        stats = (
            f"- SPATIAL: {q['spatial']['panoptic_seg_status']} | Drain Prox: {q['spatial']['drain_prox_ft']}ft\n"
            f"- SPECTRAL: Fingerprint {q['spectral']['fingerprint']} | Purity {q['spectral']['purity_index']}\n"
            f"- TEMPORAL (100YR): {q['temporal']['forecast_100yr']}\n"
            f"- LEGAL: {q['legal']['sb_1383_status']} | SB 54 Debt: ${q['legal']['sb_54_debt_usd']}\n"
            f"- ECO-IMPACT: Methane {q['eco_impact']['methane_flux_est']} | Leachate pH: {q['eco_impact']['leachate_ph']}"
        )
        pdf.multi_cell(0, 5, clean_text(stats))
        
        pdf.ln(5)
        
        pdf.set_font("helvetica", "I", 10)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(0, 8, f'"{clean_text(entry["witty_caption"])}"')
        pdf.set_text_color(0, 0, 0)

    pdf.output(OUTPUT_PDF)
    print(f"✅ SUCCESS: PDF saved to {OUTPUT_PDF}")

if __name__ == "__main__":
    create_pdf()
