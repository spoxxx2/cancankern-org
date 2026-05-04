def calculate_impedance_match(extraction_velocity, brain_fluid_velocity):
    # Target: Brain fluid is approx 1500-1600 m/s
    match_percentage = (1.0 - abs(extraction_velocity - brain_fluid_velocity) / brain_fluid_velocity) * 100
    
    print(f"--- [NODE 93307: ACOUSTIC TRANSPARENCY] ---")
    print(f"VELOCITY MATCH: {match_percentage:.2f}%")
    
    if match_percentage > 98.0:
        return "[✓] STATUS: ACOUSTIC GHOST. THE BRAIN CANNOT 'SEE' THE INJECTION."
    return "[!] STATUS: ACOUSTIC REFLECTION (Potential Inflammation)."

# 1588 m/s vs 1540 m/s (Average Brain Fluid)
print(calculate_impedance_match(1588, 1540))
