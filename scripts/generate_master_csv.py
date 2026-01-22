import os
import json
import csv

log_dir = os.path.expanduser("~/cancankern-org/logs/digital_twins/")
output_file = os.path.expanduser("~/cancankern-org/docs/compliance/MASTER_IMPACT_LEDGER.csv")

def generate():
    files = [f for f in os.listdir(log_dir) if f.endswith('.json')]
    data_rows = []
    total_kg = 0
    MARKET_PRICE_PER_TON = 28.50 # Current Carbon Credit Market Price

    headers = ["Audit_ID", "Timestamp", "Material", "CO2e_kg", "Market_Value_USD", "BSF_Yield_kg"]

    for filename in files:
        path = os.path.join(log_dir, filename)
        with open(path, 'r') as f:
            try:
                d = json.load(f)
                kg = float(d.get("environmental_impact_score", 0.45))
                total_kg += kg
                
                # Economic & Bio-conversion math
                val = (kg / 1000) * MARKET_PRICE_PER_TON
                bsf = kg * 0.20 # 20% conversion rate into larvae
                
                data_rows.append([
                    d.get("id", filename),
                    d.get("audit_timestamp", "2026-01-18"),
                    d.get("taxonomy", {}).get("material", "Organic"),
                    kg, f"${val:.4f}", f"{bsf:.2f}"
                ])
            except: continue

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data_rows)

    # Hardwire the result into the website's Hero Section
    total_val = (total_kg / 1000) * MARKET_PRICE_PER_TON
    print(f"TOTAL_KG={total_kg}")
    print(f"TOTAL_VAL={total_val:.2f}")

if __name__ == "__main__":
    generate()
