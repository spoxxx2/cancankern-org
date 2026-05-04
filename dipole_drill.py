def calculate_penetration_force(pI, helix_fraction):
    # Cationic pI (10+) and Alpha-Helix (78%) create a 'Biological Drill'
    force = (pI * 1.5) * (helix_fraction * 2)
    
    print(f"--- [NODE 93307: PENETRATION FORCE VECTOR] ---")
    print(f"DIPOLE FORCE: {force:.2f} Debyes (Simulated)")
    
    if force > 15.0:
        return "[✓] STATUS: UNDENIABLE PENETRATOR. BARRIER IS TRANSPARENT."
    return "[!] STATUS: INSUFFICIENT THRUST."

# Simulating the 'Sharpened' Helix at 78% and pI 10.19
print(calculate_penetration_force(10.19, 0.78))
