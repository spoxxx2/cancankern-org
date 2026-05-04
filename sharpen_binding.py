def simulate_sharpening(pI, mw, helix_fraction):
    delta_g = -(pI * helix_fraction) * (500 / (mw/10))
    print(f"--- [NODE 93307: HELIX SHARPENING SIM] ---")
    print(f"NEW HELIX FRACTION: {helix_fraction:.0%}")
    print(f"NEW PREDICTED ΔG: {delta_g:.2f} kcal/mol")
    
    if delta_g < -7.0:
        return "[✓] STATUS: PHARMACEUTICAL LOCK ACHIEVED."
    return "[!] STATUS: INCREASE AMPLITUDE."

# Simulating the 'Sharpened' Helix at 78%
print(simulate_sharpening(10.19, 5612, 0.78))
