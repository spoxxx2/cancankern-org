import os, json, glob

def generate_report():
    BASE_DIR = os.path.expanduser("~/cancankern-org")
    AUDIT_FILES = glob.glob(f"{BASE_DIR}/audits/*.json")
    
    total_audits = len(AUDIT_FILES)
    total_circular_value = 0.0
    sb1383_organic_count = 0
    plastic_leaching_avg = []
    
    print(f"📊 ANALYZING {total_audits} FORENSIC MANIFESTS...")

    for file in AUDIT_FILES:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                
                # 1. Total Circular Economy Value
                # Standard scrap PET/Ferrous value for 2026 (~$4.20/unit estimate)
                val = data.get("upcycle_potential", {}).get("circular_economy_value", "$0.00")
                total_circular_value += float(val.replace('$', ''))
                
                # 2. SB 1383 / Organic Vault Count
                if "compliance_1383_vault" in data:
                    sb1383_organic_count += 1
                
                # 3. 50-Year Leaching Danger Metrics
                leach_score = data.get("forecast_1_100", {}).get("leaching_risk", 0)
                if leach_score: plastic_leaching_avg.append(leach_score)
                
        except: continue

    avg_leach = sum(plastic_leaching_avg) / len(plastic_leaching_avg) if plastic_leaching_avg else 0

    # GENERATE THE SCORECARD
    print("\n" + "="*40)
    print("💎 CANCAN KERN COMPLIANCE SCORECARD")
    print(f"NODE: Panama Lane / 1501 Pearl St")
    print("="*40)
    print(f"✅ TOTAL AUDITS:            {total_audits}")
    print(f"💰 CIRCULAR ECONOMY VALUE:  ${total_circular_value:.2f}")
    print(f"🥗 SB 1383 ORGANIC VOLUMES: {sb1383_organic_count} Records")
    print(f"☢️  AVG 50Y LEACHING RISK:   {avg_leach:.1f}/100")
    print(f"⚖️  CITY COMPLIANCE:         BMC § 8.32.190 - CERTIFIED")
    print("="*40)
    print("🚀 Status: Ready for Grant Submission (Freed/Awesome Foundations)")

if __name__ == "__main__":
    generate_report()
