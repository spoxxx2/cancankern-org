from fpdf import FPDF

class CANCAN_Letter(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'COMMUNITY ACTION NETWORK, CLEAN AND NOURISH (CANCAN)', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 5, '1501 Pearl St, Bakersfield, CA 93305 | (661) 748-8251 | spoxxx2@gmail.com', 0, 1, 'C')
        self.set_font('Arial', 'I', 8)
        self.cell(0, 5, 'EIN: 39-2261270 | UEI: SSWWJ3SEMZ73 | Account: 074218 | DOI: 10.5281/zenodo.18362541', 0, 1, 'C')
        self.ln(10)
        self.line(10, 32, 200, 32)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'National Asset Status: Active | DPA Title III Framework | SB 1383 Compliance Auditor', 0, 0, 'C')

pdf = CANCAN_Letter()
pdf.add_page()
pdf.set_font('Arial', '', 11)
pdf.ln(5)
pdf.cell(0, 10, 'Date: April 4, 2026', 0, 1)
pdf.ln(5)
pdf.multi_cell(0, 5, 'TO: Federal Service Desk\nATTN: SAM.gov Registration Processing\n4100 Alpha Road\nDallas, TX 75244')
pdf.ln(10)
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 10, 'SUBJECT: Appointment of Entity Administrator for CANCAN (UEI: SSWWJ3SEMZ73)', 0, 1)
pdf.set_font('Arial', '', 11)

body_text = (
    "To Whom It May Concern,\n\n"
    "I, Casey Lee Canfield, in my capacity as the Founder and Executor of Community Action Network, "
    "Clean and Nourish (CANCAN), hereby appoint myself as the Entity Administrator.\n\n"
    "Entity Administrator Information:\n"
    "- Name: Casey Lee Canfield\n"
    "- Phone Number: (661) 748-8251\n"
    "- Email Address: spoxxx2@gmail.com\n\n"
    "This appointment is to facilitate our eligibility for Federal Awards and the issuance of a "
    "CAGE Code for upcoming Department of Energy (DOE) and National Security research initiatives. "
    "I certify that the information provided is true and correct.\n\n"
    "Sincerely,\n\n\n"
    "__________________________\n"
    "Casey Lee Canfield\n"
    "Founder & Executor, CANCAN"
)
pdf.multi_cell(0, 6, body_text)
pdf.output('CANCAN_SAM_Letter.pdf')
