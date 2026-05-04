from fpdf import FPDF
import json

class ComplianceReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'CANCAN FOOD RECOVERY & COMPLIANCE', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 5, 'Authorized per BMC § 8.32.190 | Panama Lane Node 93307', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, label, 0, 1, 'L', 1)
        self.ln(4)

def generate_pdf(data):
    pdf = ComplianceReport()
    pdf.add_page()
    
    # 1. General Info
    pdf.chapter_title('1. Audit Metadata')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, f"Log ID: {data['audit_event']['log_id']}", 0, 1)
    pdf.cell(0, 5, f"Timestamp: {data['audit_event']['timestamp']}", 0, 1)
    pdf.cell(0, 5, f"AQI Status: {data['audit_event']['aqi_report']['status']} (Index: {data['audit_event']['aqi_report']['index']})", 0, 1)
    pdf.ln(5)

    # 2. Vision Results
    pdf.chapter_title('2. AI Vision Analysis (Hybrid YOLOv12 + ViT)')
    for obj in data['objects']:
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 5, f"Object: {obj['label']}", 0, 1)
        pdf.set_font('Arial', '', 9)
        pdf.cell(0, 5, f" - Material: {obj['taxonomy']['material']} | Confidence: {obj['vi_confidence']*100}%", 0, 1)
        pdf.cell(0, 5, f" - 50-Year Forecast: {obj['forecast_50yr']['year_50']}", 0, 1)
        pdf.ln(2)

    # 3. Impact
    pdf.ln(5)
    pdf.chapter_title('3. Environmental Impact')
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, f"Diverted Weight: {data['summary']['total_diverted_kg']} kg", 0, 1)
    
    output_fn = f"Report_{data['audit_event']['log_id']}.pdf"
    pdf.output(output_fn)
    print(f"Report generated: {output_fn}")

if __name__ == "__main__":
    with open('test_audit.json', 'r') as f:
        generate_pdf(json.load(f))
