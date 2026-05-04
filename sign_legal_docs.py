import weasyprint
from weasyprint import HTML, CSS

css = """
@page { size: letter; margin: 1in; }
body { font-family: serif; font-size: 12pt; line-height: 2; }
.sig-block { margin-top: 50px; line-height: 1.5; }
h1 { text-align: center; text-transform: uppercase; }
"""

# 1. THE OATH (Most Critical)
oath_html = """
<h1>Inventor's Oath or Declaration</h1>
<p>I believe I am the original inventor or an original joint inventor of a claimed invention in the application.</p>
<div class="sig-block">
    Signature: <b>/Casey Lee Canfield/</b><br>
    Name: Casey Lee Canfield<br>
    Date: March 28, 2026
</div>
"""

# 2. MICRO ENTITY CERTIFICATION (Fee Shield)
micro_html = """
<h1>Certification of Micro Entity Status</h1>
<p>The applicant hereby certifies that they qualify as a MICRO ENTITY (Gross Income Basis) under 37 CFR 1.29(a).</p>
<div class="sig-block">
    Signature: <b>/Casey Lee Canfield/</b><br>
    Name: Casey Lee Canfield<br>
    Date: March 28, 2026
</div>
"""

# 3. TRANSMITTAL LETTER (Cover Sheet)
trans_html = """
<h1>Patent Transmittal Letter</h1>
<p>To the Commissioner for Patents: Please find the enclosed Utility Patent Application for 'Mirabestin-Delta'.</p>
<div class="sig-block">
    Respectfully submitted,<br><br>
    Signature: <b>/Casey Lee Canfield/</b><br>
    Name: Casey Lee Canfield<br>
    Address: 1501 Pearl St, Bakersfield, CA 93305
</div>
"""

# Generate PDFs
HTML(string=oath_html).write_pdf("Oath_Mirabestin.pdf", stylesheets=[CSS(string=css)])
HTML(string=micro_html).write_pdf("MicroEntity_Mirabestin.pdf", stylesheets=[CSS(string=css)])
HTML(string=trans_html).write_pdf("Transmittal_Mirabestin.pdf", stylesheets=[CSS(string=css)])

print("[SUCCESS] Signed legal docs generated.")
