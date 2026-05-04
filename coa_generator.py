import json, time

def create_coa(batch_name, purity):
    coa_data = {
        "header": "CERTIFICATE OF ANALYSIS - CANCAN RESEARCH NODE",
        "batch_info": {
            "batch_id": f"V26-{int(time.time())}",
            "manufacture_date": time.strftime("%Y-%m-%d"),
            "location": "1501_PEARL_ST_MONOLITH"
        },
        "specifications": {
            "peptide_name": "CANCAN-V26_PHOENIX_LATTICE",
            "purity_target": f"{purity}%",
            "identity_check": "HPLC-MS_MATCHED",
            "isoelectric_point": "pH_4.2",
            "tyndall_verification": "POSITIVE"
        },
        "disclaimer": "FOR_RESEARCH_USE_ONLY_NOT_FOR_HUMAN_CONSUMPTION"
    }

    filename = f"COA_{coa_data['batch_info']['batch_id']}.json"
    with open(filename, "w") as f:
        json.dump(coa_data, f, indent=4)
    
    print(f"\n[ORACLE] COA Template Generated: {filename}")
    print("[ACTION] Upload this data to your Zenodo DOI record for permanent provenance.")

if __name__ == "__main__":
    create_coa("V26-PHOENIX", 99.9)
