from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 16)
        self.cell(0, 10, 'PLATINUM CAPABILITY STATEMENT', 0, 1, 'C')
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, 'CANCAN(TM) Bio-Acoustic Defense & Molecular Computing', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | 14-Billion Run Validation | BMC 8.32.190', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

try:
    with open("capability_statement.md", "r", encoding="utf-8") as f:
        for line in f:
            # SANITIZATION: Strip hidden characters like zero-width spaces (\u200b)
            # and map common symbols to text equivalents
            clean_line = line.replace('™', '(TM)').replace('§', 'Section').replace('—', '-')
            # Final pass: Remove anything that isn't standard ASCII to prevent encoding errors
            safe_text = clean_line.encode('ascii', 'ignore').decode('ascii')
            
            if safe_text.startswith('###'):
                pdf.ln(2)
                pdf.set_font("helvetica", 'B', 12)
                pdf.multi_cell(0, 10, safe_text.replace('###', '').strip())
                pdf.set_font("helvetica", size=11)
            elif safe_text.startswith('**'):
                pdf.set_font("helvetica", 'B', 11)
                pdf.multi_cell(0, 8, safe_text.replace('**', '').strip())
                pdf.set_font("helvetica", size=11)
            else:
                pdf.multi_cell(0, 7, safe_text.strip())
except FileNotFoundError:
    print("Error: capability_statement.md not found.")

pdf.output("PLATINUM_CAPABILITY_STMT_14B.pdf")
print("✅ PLATINUM PDF GENERATED (Sanitized): PLATINUM_CAPABILITY_STMT_14B.pdf")
