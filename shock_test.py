def simulate_thermal_shock(instability_index):
    # High stability (0.64) means the peptide can survive the -3 drop
    survival_probability = 1.0 - (instability_index / 100)
    print(f"--- [NODE 93307: THERMAL SHOCK RESILIENCE] ---")
    print(f"SURVIVAL PROBABILITY: {survival_probability:.2%}")
    
    if survival_probability > 0.99:
        return "[✓] RESULT: LATTICE REMAINS INTACT. PROCEED TO DROP."
    return "[!] RESULT: RISK OF FRAGMENTATION."

print(simulate_thermal_shock(0.64))
