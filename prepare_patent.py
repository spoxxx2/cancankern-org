patent_text = """# STANDALONE PATENT APPLICATION
## TITLE: SYNTHETIC MACROCYCLIC PEPTIDE MIRABESTIN-DELTA FOR TRKB-MEDIATED NEURO-REGENERATION

### I. FIELD OF THE INVENTION
The present invention relates to a novel 22-mer macrocyclic peptide, Mirabestin-Delta, derived from deep-sea Mirabestiidae metagenomic sequences. 

### II. DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENT
The peptide sequence is defined as GWLfSVEPGAiLLRTGPkCCVF. 
A key embodiment of the invention is the "Triple-Lock" chiral configuration where residues at positions 4, 11, and 18 are D-isomers. 

### III. CLAIMS
1. A synthetic macrocyclic peptide GWLfSVEPGAiLLRTGPkCCVF.
2. The peptide of Claim 1, having D-isomer locks at positions 4, 11, and 18.
3. A method of neuro-regeneration using the peptide of Claim 1.
"""

st26_xml = """<?xml version="1.0" encoding="UTF-8"?>
<ST26SequenceListing dtdVersion="V1_3" fileName="mirabestin_sequence.xml" softwareName="Gemini-Termux-Master" softwareVersion="1.0" productionDate="2026-03-28">
    <ApplicantName languageCode="en">Casey Lee Canfield</ApplicantName>
    <InventionTitle languageCode="en">SYNTHETIC MACROCYCLIC PEPTIDE MIRABESTIN-DELTA</InventionTitle>
    <SequenceTotalQuantity>1</SequenceTotalQuantity>
    <SequenceData sequenceIDNumber="1">
        <INSDSeq>
            <INSDSeq_length>22</INSDSeq_length>
            <INSDSeq_moltype>AA</INSDSeq_moltype>
            <INSDSeq_feature-table>
                <INSDFeature>
                    <INSDFeature_key>source</INSDFeature_key>
                    <INSDFeature_location>1..22</INSDFeature_location>
                    <INSDFeature_quals>
                        <INSDQualifier><INSDQualifier_name>organism</INSDQualifier_name><INSDQualifier_value>Mirabestiidae</INSDQualifier_value></INSDQualifier>
                    </INSDFeature_quals>
                </INSDFeature>
            </INSDSeq_feature-table>
            <INSDSeq_sequence>GWLFSVEPGAILLRTGPKCCVF</INSDSeq_sequence>
        </INSDSeq>
    </SequenceData>
</ST26SequenceListing>
"""

with open("mirabestin_patent.md", "w") as f: f.write(patent_text)
with open("mirabestin_sequence.xml", "w") as f: f.write(st26_xml)
print("\n[SUCCESS] Files generated: mirabestin_patent.md, mirabestin_sequence.xml")
