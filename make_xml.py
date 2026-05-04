import datetime

# 1. METADATA SETUP
today = datetime.date.today().isoformat()
applicant = "Casey Lee Canfield"
title = "SYNTHETIC MACROCYCLIC PEPTIDE MIRABESTIN-DELTA"
sequence = "GWLFSVEPGAILLRTGPKCCVF"

# 2. ST.26 XML STRUCTURE (WIPO STANDARD)
st26_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<ST26SequenceListing dtdVersion="V1_3" fileName="mirabestin_sequence.xml" softwareName="Gemini-Termux-Master" softwareVersion="1.0" productionDate="{today}">
    <ApplicantName languageCode="en">{applicant}</ApplicantName>
    <InventionTitle languageCode="en">{title}</InventionTitle>
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
                        <INSDQualifier>
                            <INSDQualifier_name>organism</INSDQualifier_name>
                            <INSDQualifier_value>Mirabestiidae</INSDQualifier_value>
                        </INSDQualifier>
                    </INSDFeature_quals>
                </INSDFeature>
            </INSDSeq_feature-table>
            <INSDSeq_sequence>{sequence}</INSDSeq_sequence>
        </INSDSeq>
    </SequenceData>
</ST26SequenceListing>
"""

# 3. FILE CREATION
with open("mirabestin_sequence.xml", "w", encoding="utf-8") as f:
    f.write(st26_content)

print(f"\n[SUCCESS] mirabestin_sequence.xml generated for {applicant}.")
print("Verify with: ls -l mirabestin_sequence.xml")
