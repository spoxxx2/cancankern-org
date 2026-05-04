import os, json
from datetime import datetime

def get_battery():
    try:
        # Siphoning capacity directly from the kernel
        with open("/sys/class/power_supply/battery/capacity", "r") as f:
            return int(f.read().strip())
    except: return 100

def get_temp():
    try:
        # Siphoning CPU thermal zone
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            return int(f.read().strip()) / 1000
    except: return 0

def check_node_vitals():
    percent = get_battery()
    temp = get_temp()
    
    status = "OPTIMAL"
    if temp > 45 or percent < 15:
        status = "CRITICAL_LIMIT"
    
    vitals = {
        "timestamp": str(datetime.now()),
        "cpu_temp": temp,
        "battery_level": percent,
        "node_status": status,
        "resonance": "650.12Hz"
    }
    
    with open('node_vitals.json', 'w') as f:
        json.dump(vitals, f, indent=4)
    
    if status == "CRITICAL_LIMIT":
        print(f"!! IMPERIAL ALERT: Node at {temp}C / {percent}% Battery. RESISTANCE DETECTED.")
        return False
    print(f"Node Vitals: {temp}C | {percent}% Power | Resonance: 650.12Hz - {status}")
    return True

if __name__ == "__main__":
    check_node_vitals()
