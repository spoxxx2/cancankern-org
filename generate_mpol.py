from fpdf import FPDF

class MPoL_PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(0, 10, "National Security Asset Technical Brief: MPoL-93307", border=False, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()} | Panama Lane Node | BMC § 8.32.190 Compliance", align="C")

def create_pdf():
    pdf = MPoL_PDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, "1. Asset Identification", ln=True)
    pdf.set_font("helvetica", size=10)
    pdf.multi_cell(0, 10, "ID: PANAMA-LANE-NODE-93307\nOperator: Casey Lee Canfield\nOrg: CANCAN (Non-Profit)\nLocation: Kern San Joaquin Valley Air Basin")
    
    pdf.ln(5)
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, "2. Mathematical Proof of Mechanism", ln=True)
    pdf.set_font("courier", size=10)
    equation = "dP/dt = k * (Csat - P(t)) + Integral[Phi(w, a)] dt"
    pdf.multi_cell(0, 10, f"Extraction Flux: {equation}\nValidation: 1,000,000,000 Simulation Runs\nConfidence Interval: 99.4%")
    
    pdf.ln(5)
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, "3. 50-Year Degradation Forecast", ln=True)
    pdf.set_font("helvetica", size=10)
    pdf.cell(40, 10, "Year", 1)
    pdf.cell(60, 10, "Oxidation Level", 1)
    pdf.cell(60, 10, "Worth (Estimated)", 1, ln=True)
    
    data = [["10", "12.5%", "Appreciating"], ["25", "48.0%", "Strategic"], ["50", "94.2%", "Inert/Converted"]]
    for row in data:
        pdf.cell(40, 10, row[0], 1)
        pdf.cell(60, 10, row[1], 1)
        pdf.cell(60, 10, row[2], 1, ln=True)

    pdf.output("National_Asset_MPoL_93307.pdf")
    print("\n--- SUCCESS ---")
    print("PDF Generated: National_Asset_MPoL_93307.pdf")

if __name__ == "__main__":
    create_pdf()
