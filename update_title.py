import weasyprint
from weasyprint import HTML, CSS

title = "SYNTHETIC MACROCYCLIC PEPTIDE MIRABESTIN-DELTA AND BIO-ACOUSTIC INDUCTION METHOD FOR NEURO-REGENERATIVE SYNTHESIS"

css = "@page { size: letter; margin: 1in; } body { font-family: serif; font-size: 12pt; line-height: 2; } h1 { text-align: center; text-transform: uppercase; font-size: 14pt; }"

# Updating the Specification header
spec_html = f"<h1>{title}</h1><h2>Specification</h2><p>The present invention relates to bio-acoustic induction of peptide synthesis...</p>"

weasyprint.HTML(string=spec_html).write_pdf("Spec_Mirabestin.pdf", stylesheets=[weasyprint.CSS(string=css)])
print(f"[SUCCESS] Title Synced: {title}")
