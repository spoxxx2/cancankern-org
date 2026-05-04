import os

# 1. TRANSMITTAL LETTER (PTO/AIA/15)
transmittal_content = """# UTILITY PATENT APPLICATION TRANSMITTAL
**TO:** Commissioner for Patents, P.O. Box 1450, Alexandria, VA 22313-1450

**INVENTOR:** Casey Lee Canfield  
**TITLE:** SYNTHETIC MACROCYCLIC PEPTIDE MIRABESTIN-DELTA  
**DATE:** March 28, 2026

### ENCLOSED APPLICATION PAPERS:
1. **Fee Transmittal Form** (Small Entity / Micro Entity)
2. **Specification** (including Description, Claims, and Abstract)
3. **Sequence Listing** (ST.26 XML format)
4. **Application Data Sheet** (PTO/AIA/14)

### DECLARATION:
The undersigned hereby asserts **Micro Entity Status** under 37 CFR 1.29.
"""

# 2. FEE WORKSHEET (2026 MARCH RATES)
fee_worksheet = """# PATENT FEE ESTIMATE (MICRO ENTITY) - MARCH 2026
**Entity Status:** Micro Entity (80% Reduction)

| Fee Description | Fee Code | Amount |
| :--- | :--- | :--- |
| Basic Filing Fee (Utility) | 1011/2011/3011 | $64.00 |
| Utility Search Fee | 1111/2111/3111 | $140.00 |
| Utility Examination Fee | 1311/2311/3311 | $160.00 |
| **TOTAL ESTIMATED FILING FEES** | | **$364.00** |

*Note: DOCX filing avoids the $86 non-DOCX surcharge.*
"""

with open("transmittal_letter.md", "w") as f: f.write(transmittal_content)
with open("fee_worksheet.md", "w") as f: f.write(fee_worksheet)

print("[SUCCESS] Markdown forms created.")
