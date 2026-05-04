import json
import os

# Configuration
PRO_EMAIL = "serviceproviders.support@circularactionalliance.org"
DIVERSION_REPORT = "pro_compliance_report.json"

if not os.path.exists(DIVERSION_REPORT):
    print(f"Error: {DIVERSION_REPORT} not found. Run aggregate_audits.py first.")
    exit()

with open(DIVERSION_REPORT, 'r') as f:
    data = json.load(f)

# Extract metrics
total_kg = data.get('total_diverted_kg', 0)
sb54_count = data.get('compliance_summary', {}).get('sb54_eligible', 0)
top_brand = max(data.get('brands', {}), key=data.get('brands', {}).get) if data.get('brands') else "N/A"

email_body = f"""
Subject: Verified SB 54 Diversion Data - Panama Lane Node Audit

To Circular Action Alliance Support Team,

I am writing on behalf of a non-profit food recovery and upcycling operation in Bakersfield, CA (93307). 

We currently operate an AI-driven vision stack (Hybrid YOLOv12 + ViT) at our Panama Lane Node, generating Digital Twin metadata for all processed waste streams. We have identified significant quantities of SB 54 Covered Materials that we are successfully diverting from the Kern San Joaquin Valley landfill through circular economy pathways and BSFL bioconversion.

Current Audit Summary (Last 60 Days):
- Total Weight Diverted: {total_kg} kg
- SB 54 Eligible Components: {sb54_count} verified units
- Primary Brand Liability Detected: {top_brand}

Our audits include panoptic segmentation and 500-year environmental impact forecasting, compliant with BMC § 8.32.190. We are interested in providing this brand-level compliance data to your producers to assist with their 2026 reporting obligations.

Please let us know the process for authorized data service providers under the California SB 54 program.

Best regards,

[Your Name]
Panama Lane Node Operator
"""

print("--- PRO PITCH DRAFT GENERATED ---")
print(email_body)
print(f"--- END DRAFT (Send to: {PRO_EMAIL}) ---")
