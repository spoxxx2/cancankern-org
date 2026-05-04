import json
import random

def simulate_batch(lot_id, freq, temp):
    # ACS Grade Simulation Logic
    # Higher frequency stress (400-800Hz) correlates to higher Peptide Yield
    yield_factor = (freq / 800) * 0.95 
    purity = 98.5 + random.uniform(-0.5, 0.5)
    
    return {
        "lot_number": lot_id,
        "parameters": {"freq_hz": freq, "temp_c": temp},
        "results": {
            "amp_yield_mg_g": round(yield_factor * 12.5, 2),
            "purity_acs": f"{purity:.2f}%",
            "residue_after_evap": "0.0008%",
            "reproducibility_index": "Pass"
        }
    }

# Compare Lot 001 (Control) vs Lot 002 (Active Stress)
lot_a = simulate_batch("20260212-A", 0, 25.5)
lot_b = simulate_batch("20260212-B", 650, 28.2)

print("--- DIGITAL TWIN COMPARISON ---")
print(f"LOT A (No Stress): {lot_a['results']['amp_yield_mg_g']} mg/g")
print(f"LOT B (650Hz Stress): {lot_b['results']['amp_yield_mg_g']} mg/g")
print(f"Yield Increase: {((lot_b['results']['amp_yield_mg_g']/lot_a['results']['amp_yield_mg_g'])-1)*100:.1f}%")
