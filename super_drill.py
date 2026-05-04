def boost_penetration(force, mag_alignment):
    # mag_alignment (0.0 to 1.0) represents the Earth's field lock at Node 93307
    boosted_force = force * (1 + (mag_alignment * 0.15))
    
    print(f"--- [NODE 93307: SUPER-DRILL ENHANCEMENT] ---")
    print(f"ENHANCED DIPOLE FORCE: {boosted_force:.2f} Debyes")
    
    if boosted_force > 27.0:
        return "[✓] STATUS: HYPER-PENETRATOR. BARRIER RESISTANCE IS ZERO."
    return "[!] STATUS: INCREASE MAGNETIC COHERENCE."

# Boosting the 23.84 Force with a 90% Magnetic Lock
print(boost_penetration(23.84, 0.90))
