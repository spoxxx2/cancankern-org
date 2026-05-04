import json
import os

def calculate_eis(organic_mass_kg, duration_hrs):
    # Standard SB 1383 Diversion Factor (Estimated)
    # 1kg organic waste = ~0.5kg CO2e avoided in landfill
    co2_offset = organic_mass_kg * 0.5
    
    # Bio-Acoustic Efficiency Multiplier (650Hz Sawtooth)
    # We calibrate this based on your 5-wave strategy
    efficiency_score = (duration_hrs / 3.0) * 1.2 
    
    impact_score = co2_offset * efficiency_score
    return round(impact_score, 2)

if __name__ == "__main__":
    # Placeholder: Input 2.5kg for the current Pearl St. run
    mass = 2.5 
    score = calculate_eis(mass, 3)
    print(f"[+] Environmental Impact Score: {score} CO2e units")
    
    # Append to your Digital Twin log
    with open(os.path.expanduser('~/gemini.md'), 'a') as f:
        f.write(f"\n- [2026-04-01] Run Complete: {mass}kg processed. EIS: {score}\n")
