import json, os

# Config
JSON_PATH = "/storage/emulated/0/Documents/CANCAN_AUDITS/HYPER_MASTER_LEDGER.json"

def generate_prospectus():
    if not os.path.exists(JSON_PATH):
        print("❌ Hyper-Ledger not found!")
        return

    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    total_assets = len(data)
    
    # Financial Drivers
    avoided_fines = 0  # SB 1383 / BMC 8.32.190
    commodity_value = 0 # Protein/Compost potential
    insurance_risk_offset = 0 # Fire/Leachate prevention
    carbon_credit_potential = 0 # Methane abatement

    for entry in data:
        q = entry['quintuplet']
        
        # 1. Government Value (Fines avoided)
        avoided_fines += entry['quintuplet']['legal_liability'].get('sb_1383_fine_est', 250)
        
        # 2. Private Value (BSFL Protein Commodity)
        # 1 ton of food waste = ~$200 in BSFL protein meal
        commodity_value += 12.50 # Avg value per "audit event" volume
        
        # 3. Insurance Value (Loss control)
        if q['environmental_debt'].get('thermal_anomaly_risk') == "CRITICAL_FIRE_RISK":
            insurance_risk_offset += 5000 # Cost of a minor dumpster fire
        else:
            insurance_risk_offset += 50 

        # 4. Carbon Market (High-Fidelity Insetting)
        # $40 per tonne of CO2e
        carbon_credit_potential += 8.25

    print("\n" + "="*45)
    print("💼 CANCAN OMNI-BUYER FISCAL PROSPECTUS")
    print("="*45)
    print(f"Total Forensic Assets: {total_assets}")
    print(f"Node Location: 1501 Pearl St / 93307")
    print("-" * 45)
    print(f"🏛️ GOV VALUE (Avoided Fines):    ${avoided_fines:,.2f}")
    print(f"🏢 PRIVATE VALUE (Commodities):  ${commodity_value:,.2f}")
    print(f"🛡️ INSURANCE VALUE (Risk):       ${insurance_risk_offset:,.2f}")
    print(f"🌱 CARBON VALUE (Insetting):    ${carbon_credit_potential:,.2f}")
    print("-" * 45)
    print(f"🚀 TOTAL DATASET VALUATION:      ${(avoided_fines + commodity_value + insurance_risk_offset + carbon_credit_potential):,.2f}")
    print("="*45)
    print("💡 Wit: If you aren't counting it, you aren't owning it.")

if __name__ == "__main__":
    generate_prospectus()
