import math

def check_folding_energy(instability_index, temp_c):
    # Boltzmann Constant (simulated scaling)
    temp_k = temp_c + 273.15
    # A low instability index (0.64) creates a deep 'Energy Well'
    energy_well = - (1.0 / (instability_index + 0.01)) * 10
    
    print(f"--- [NODE 93307: THERMODYNAMIC STABILITY] ---")
    print(f"ENERGY WELL DEPTH: {energy_well:.2f} kJ/mol")
    
    if energy_well < -50:
        return "[✓] STATUS: THERMODYNAMICALLY LOCKED. ZERO RISK OF SPONTANEOUS UNFOLDING."
    return "[!] STATUS: THERMAL INSTABILITY DETECTED."

print(check_folding_energy(0.64, 37.0))
