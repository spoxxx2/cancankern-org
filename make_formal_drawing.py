import weasyprint
from weasyprint import HTML, CSS

drawing_css = """
@page { 
    size: letter; 
    margin: 1in 0.75in 0.75in 1in; 
}
body { font-family: sans-serif; text-align: center; }
.header { text-align: right; font-size: 10pt; margin-bottom: 50px; }
.figure-container { border: 1px solid #ccc; padding: 40px; margin: 0 auto; width: 80%; position: relative; }
.block { border: 2px solid black; margin: 15px auto; padding: 10px; width: 60%; font-weight: bold; }
.arrow { font-size: 20pt; line-height: 1; }
.ref-num { font-size: 10pt; font-weight: normal; color: blue; }
"""

html_content = """
<div class="header">Sheet 1 of 1</div>
<h1>FIG. 1</h1>
<div class="figure-container">
    <div class="block">Sawtooth Wave Generator (650 Hz)<br><span class="ref-num">10</span></div>
    <div class="arrow">↓</div>
    <div class="block">Digital-to-Analog Converter / Amp<br><span class="ref-num">20</span></div>
    <div class="arrow">↓</div>
    <div class="block">Acoustic Transducers / Exciters<br><span class="ref-num">30</span></div>
    <div class="arrow">↓</div>
    <div class="block">Bio-Expression Matrix (BSFL)<br><span class="ref-num">40</span></div>
</div>
<p style="margin-top: 50px;"><b>Inventor:</b> Casey Lee Canfield</p>
"""

weasyprint.HTML(string=html_content).write_pdf(
    "Drawing_Mirabestin.pdf", 
    stylesheets=[weasyprint.CSS(string=drawing_css)]
)
print("[SUCCESS] Formal Drawing Generated: Drawing_Mirabestin.pdf")
