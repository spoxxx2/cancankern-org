import requests
import json
import os

def broadcast_audit(audit_json):
    """
    Directly pushes Digital Twin metadata to cancankern.org
    Target: Azure cancan-backend | Node: Panama Lane 93307
    Compliance: BMC § 8.32.190
    """
    url = "https://cancan-backend.azurewebsites.net/api/v1/twin-sync"
    
    # Ensuring the 50-year forecast and AQI safety are present
    if "forecasting_50_year" not in audit_json:
        print("Warning: Missing 50-year forecast. Compliance risk.")

    try:
        # Check AQI from metadata to trigger 'Mask Required' flag on site
        if audit_json['audit_metadata']['environmental_conditions']['aqi'] > 100:
            audit_json['audit_metadata']['environmental_conditions']['safety_protocol'] = "Mask Required"

        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=audit_json, timeout=10)
        
        if r.status_code == 200:
            print(f"Digital Twin Synced. Impact Score: {audit_json.get('environmental_impact_score')}")
        else:
            print(f"Sync Error {r.status_code}: Check cancan-rg resource group logs.")
            
    except Exception as e:
        print(f"Connection failed to Azure Panama Lane Node: {e}")

if __name__ == "__main__":
    # Test block
    print("Sync module active. Ready for 'aud' alias integration.")
