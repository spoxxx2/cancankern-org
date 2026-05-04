import os

files = {
    "01_Abstract.md": "# ABSTRACT\n\nA synthetic 22-mer macrocyclic peptide, designated Mirabestin-Delta, is disclosed for the induction of neuro-regenerative pathways. The peptide comprises the sequence GWLfSVEPGAiLLRTGPkCCVF, characterized by a specific triple-chiral lock configuration at positions 4, 11, and 18...",
    
    "02_Specification.md": "# SPECIFICATION\n\n## FIELD OF THE INVENTION\nThe present invention relates to bio-acoustic induction of peptide synthesis...\n\n## BACKGROUND\nDeep-sea Mirabestiidae metagenomics provide a novel frontier for TrkB agonism...",
    
    "03_Claims.md": "# CLAIMS\n\n1. A synthetic macrocyclic peptide comprising the sequence GWLfSVEPGAiLLRTGPkCCVF.\n2. The peptide of claim 1, wherein residues 4, 11, and 18 are D-isomers.\n3. A method of treatment using the peptide of claim 1...",
    
    "04_Oath.md": "# INVENTOR'S OATH OR DECLARATION (37 CFR 1.63)\n\nI believe I am the original inventor or an original joint inventor of a claimed invention in the application.\n\n**NAME:** Casey Lee Canfield\n**SIGNATURE:** /Casey Lee Canfield/\n**DATE:** March 28, 2026",
    
    "05_MicroEntity.md": "# CERTIFICATION OF MICRO ENTITY STATUS\n\nThe applicant hereby certifies that they qualify as a MICRO ENTITY (Gross Income Basis) under 37 CFR 1.29(a)..."
}

for filename, content in files.items():
    with open(filename, "w") as f:
        f.write(content)
print("Markdown sources created.")
