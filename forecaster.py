import json
from datetime import datetime

def generate_twin_log(material, subtype):
    # Hardwired 50-Year Forecast Logic
    forecasts = {
        "Ferrous Metal": {
            "50_year_appearance": "Total structural failure; disintegrated into iron oxide flakes.",
            "50_year_danger": "Moderate - High iron concentration in local soil.",
            "50_year_worth": "$0.00"
        },
        "Polymer": {
            "50_year_appearance": "Micro-plastic fragmentation; 40% mass loss.",
            "50_year_danger": "High - Chemical leaching into groundwater.",
            "50_year_worth": "$0.00"
        }
    }

    data = {
        "detection_event": {
            "timestamp": datetime.now().isoformat(),
            "audit_alias": "aud_v++"
        },
        "taxonomy": {
            "level_1_material": material,
            "level_2_subtype": subtype,
            "level_3_condition": "Found in Field",
            "level_4_disposal": "Pending Audit"
        },
        "forecast_50_year": forecasts.get(material, {"appearance": "Unknown", "danger": "Unknown", "worth": "$0.00"}),
        "environmental_impact_score": "CALCULATING..."
    }
    
    with open('audit_success.log', 'a') as f:
        f.write(json.dumps(data, indent=2) + "\n---\n")
    print(f"✅ Digital Twin Logged: {material} ({subtype})")

# Example trigger
generate_twin_log("Ferrous Metal", "Steel Can")
