from fpdf import FPDF

class PatentDoc(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "USPTO SUPPLEMENTAL DISCLOSURE: #63/986,721", border=0, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()} - Node 1501-P Confidential", align="C")

pdf = PatentDoc()
pdf.add_page()
pdf.set_font("times", size=12)

# Title
pdf.set_font("times", "B", 14)
pdf.cell(0, 10, "Structure of PHX-01 Synthetic Peptide", ln=True)
pdf.ln(5)

# Sequence Table
pdf.set_font("courier", size=12)
# Using your validated 12-mer sequence
sequence = "GLY-ALA-VAL-LEU-ILE-PHE-TRP-MET-SER-THR-TYR-ASN"
pdf.multi_cell(0, 10, f"Sequence Map:\n{sequence}", border=1)

# Resonant Parameters
pdf.ln(10)
pdf.set_font("times", "B", 12)
pdf.cell(0, 10, "Calculated Resonant Synthesis Parameters:", ln=True)
pdf.set_font("times", size=12)
pdf.multi_cell(0, 10, "* Frequency: 1.7 kHz\n* Coupling Time: 20 min\n* Induction Method: Dayton Exciter PWM\n* Node Location: 1501 Pearl St, Bakersfield")

pdf.output("PHX_01_Disclosure.pdf")
print("Successfully generated: PHX_01_Disclosure.pdf")
