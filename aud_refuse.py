import json, datetime, os

def log_refusal(store_name, address):
    log_entry = {
        "event": "Compliance_Refusal",
        "store": store_name,
        "address": address,
        "timestamp": datetime.datetime.now().isoformat(),
        "notes": "Manager refused Good-Faith audit. Flagged for City Reporting.",
        "authority": "BMC § 8.32.190",
        "ein": "39-2261270"
    }
    
    filename = f"REFUSAL_{store_name.replace(' ', '_')}.json"
    with open(os.path.expanduser(f"~/cancankern-org/audits/refusals/{filename}"), 'w') as f:
        json.dump(log_entry, f, indent=4)
    print(f"✅ STORE BLACKLISTED: {store_name}. Data ready for city enforcement.")

if __name__ == "__main__":
    s_name = input("Enter Store Name: ")
    s_addr = input("Enter Address: ")
    log_refusal(s_name, s_addr)
