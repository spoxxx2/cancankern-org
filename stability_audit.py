import math
import datetime

def calculate_stability(temp_c, purity_initial):
    # Arrhenius Equation Simulation: k = Ae^(-Ea/RT)
    # Higher temps accelerate peptide denaturation
    activation_energy = 50000  # J/mol (Simulated for BSFL AMPs)
    gas_constant = 8.314
    temp_k = temp_c + 273.15
    
    # Degradation Rate
    rate_k = math.exp(-activation_energy / (gas_constant * temp_k))
    half_life_days = round(0.693 / (rate_k * 10**6), 1) # Scaled for simulation
    
    return {
        "storage_temp_c": temp_c,
        "purity_at_t0": f"{purity_initial}%",
        "predicted_half_life_days": half_life_days,
        "expiration_date": (datetime.datetime.now() + datetime.timedelta(days=half_life_days)).strftime("%Y-%m-%d"),
        "50_year_status": "Complete Mineralization" if half_life_days < 18250 else "Stable Crystal"
    }

# Simulation for Lot 20260212-B at Pearl St Storage
print("--- SOP-AMP-004: Stability Study ---")
room_temp = calculate_stability(22.0, 98.5)
fridge_temp = calculate_stability(4.0, 98.5)

print(f"Room Temp (22°C) Shelf Life: {room_temp['predicted_half_life_days']} days (Exp: {room_temp['expiration_date']})")
print(f"Cold Chain (4°C) Shelf Life: {fridge_temp['predicted_half_life_days']} days (Exp: {fridge_temp['expiration_date']})")
