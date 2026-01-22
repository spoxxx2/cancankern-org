import json
import datetime
import os

def generate_mock_twin():
    print("--- SIMULATING HYBRID YOLOv12 + ViT AUDIT ---")
    
    # Define the data
    mock_data = {
        "detection_event": datetime.datetime.now().isoformat(),
        "objects": [
            {
                "label": "Item_001",
                "taxonomy": {
                    "material": "Cellulose",
                    "sub_type": "Corrugated Cardboard",
                    "condition": "Wet/Soiled",
                    "disposal": "Compost"
                },
                "forecast_50yr": {
                    "appearance": "Fully decomposed / Humus",
                    "estimated_worth": "$0.00 (Soil enrichment)",
                    "danger_level": "Low (Organic methane risk if anaerobic)"
                },
                "contamination_risk": "High (Wet material)"
            }
        ],
        "environmental_impact_score": 8.5
    }
    
    # Ensure the directory exists
    dir_path = os.path.expanduser("~/cancankern-org/docs")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
    file_path = os.path.join(dir_path, "mock_audit_log.json")
    
    with open(file_path, "w") as f:
        json.dump(mock_data, f, indent=4)
    
    print(f"✅ Mock Digital Twin Generated: {file_path}")
    print(json.dumps(mock_data, indent=2))

if __name__ == "__main__":
    generate_mock_twin()
