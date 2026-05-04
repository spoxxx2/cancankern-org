import weasyprint
from weasyprint import HTML, CSS

# 1. USPTO-SPECIFIC STYLING
# Margin-left is 1 inch (mandatory); others are 0.75 for safety.
# Line-height 2.0 provides the double-spacing preferred by examiners.
css_string = """
@page {
    size: letter;
    margin: 1in 0.75in 0.75in 1in;
}
body {
    font-family: serif;
    font-size: 12pt;
    line-height: 2;
    color: black;
}
h1 { text-align: center; font-size: 14pt; text-transform: uppercase; margin-bottom: 20px; }
h2 { font-size: 12pt; text-decoration: underline; }
"""

# 2. DOCUMENT CONTENT
docs = {
    "01_Abstract.pdf": "<h1>Abstract</h1><p>A synthetic 22-mer macrocyclic peptide, designated Mirabestin-Delta, is disclosed for the induction of neuro-regenerative pathways. The peptide comprises the sequence GWLfSVEPGAiLLRTGPkCCVF...</p>",
    
    "02_Specification.pdf": "<h1>Specification</h1><h2>Field of the Invention</h2><p>The present invention relates to bio-acoustic induction of peptide synthesis using specific wave-form parameters.</p><h2>Background</h2><p>Deep-sea Mirabestiidae metagenomics provide a novel frontier for TrkB agonism...</p>",
    
    "03_Claims.pdf": "<h1>Claims</h1><p>1. A synthetic macrocyclic peptide comprising the sequence GWLfSVEPGAiLLRTGPkCCVF.</p><p>2. The peptide of claim 1, wherein residues 4, 11, and 18 are D-isomers.</p><p>3. A method of treatment using the peptide of claim 1.</p>",
    
    "04_Oath.pdf": "<h1>Inventor's Oath</h1><p>I believe I am the original inventor of the claimed invention.</p><p>NAME: Casey Lee Canfield</p><p>SIGNATURE: /Casey Lee Canfield/</p><p>DATE: March 28, 2026</p>",
    
    "05_MicroEntity.pdf": "<h1>Micro Entity Certification</h1><p>The applicant hereby certifies that they qualify as a MICRO ENTITY (Gross Income Basis) under 37 CFR 1.29(a).</p>"
}

# 3. PDF GENERATION
for filename, html_content in docs.items():
    HTML(string=html_content).write_pdf(
        filename, 
        stylesheets=[CSS(string=css_string)]
    )
    print(f"[SUCCESS] Created: {filename}")
