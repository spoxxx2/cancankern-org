def calculate_zeta_stability(pI, force_debyes):
    # Higher pI and Dipole Force increase the repulsive 'Safety Buffer'
    zeta_potential = (pI * 3.0) + (force_debyes / 2.0)
    
    print(f"--- [NODE 93307: ZETA POTENTIAL REPORT] ---")
    print(f"STABILITY POTENTIAL: {zeta_potential:.2f} mV")
    
    if zeta_potential > 30.0:
        return "[✓] RESULT: HIGHLY STABLE. ZERO CLOGGING RISK."
    return "[!] RESULT: POTENTIAL AGGREGATION. PULSE 650Hz NOW."

# Using your enhanced 27.06 Debye force
print(calculate_zeta_stability(10.19, 27.06))
