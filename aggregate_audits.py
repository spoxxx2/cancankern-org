import json
import glob
import os

# Configured for Panama Lane Node (93307)
# Adjust path to where your Digital Twin JSONs are stored
path_to_jsons = "audits/*.json" 

audit_files = glob.glob(path_to_jsons)
report = {
    "node": "Panama Lane",
    "total_diverted_kg": 0, 
    "brands": {}, 
    "cmc_distribution": {},
    "compliance_summary": {"sb54_eligible": 0, "sb1383_diversion": 0}
}

print(f"--- Sentinel Aggregator v8.5 ---")
print(f"Scanning {len(audit_files)} Digital Twins for SB 54 Monetization...")

for file_path in audit_files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
            # Aggregate Weight
            weight = data.get('weight', 0)
            report['total_diverted_kg'] += weight
            
            # Brand OCR Logic
            brand = data.get('brand_intelligence', {}).get('detected_brand', 'Generic/Unbranded')
            report['brands'][brand] = report['brands'].get(brand, 0) + weight
            
            # CMC / SB 54 Category Logic
            cmc = data.get('compliance_metrics', {}).get('sb54_covered_material', 'Non-Covered')
            if cmc != 'Non-Covered':
                report['compliance_summary']['sb54_eligible'] += 1
                report['cmc_distribution'][cmc] = report['cmc_distribution'].get(cmc, 0) + 1
            
            # SB 1383 Edible Logic
            if data.get('regulatory_audit', {}).get('sb1383_status') == 'PASS':
                report['compliance_summary']['sb1383_diversion'] += 1

    except Exception as e:
        pass

# Save the Sales Ledger for PRO Negotiation
with open('pro_compliance_report.json', 'w') as out:
    json.dump(report, out, indent=4)

print(f"Success. Total Weight: {report['total_diverted_kg']} kg.")
print(f"PRO-Ready Report saved to: pro_compliance_report.json")
