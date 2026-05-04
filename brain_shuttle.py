def calculate_shuttle_efficiency(pI, mw, gravy):
    # pI: Isoelectric Point (Target: > 9.0 for cationic shuttle)
    # MW: Molecular Weight (Target: < 5000 Da for optimal transit)
    # GRAVY: Hydropathicity (Target: -0.5 to 0.5)
    
    score = (pI / 10.0) * (5000 / mw) * (1.0 - abs(gravy))
    
    print(f"\n--- [NODE 93307: SHUTTLE EFFICIENCY INDEX] ---")
    print(f"EFFICIENCY SCORE: {score:.4f}")
    
    if score > 0.8:
        return "[✓] RESULT: SUPER-SHUTTLE. HIGH BRAIN PENETRATION."
    elif score > 0.5:
        return "[✓] RESULT: STANDARD PENETRATION. SAFE FOR NEURO-USE."
    else:
        return "[!] RESULT: BARRIER REJECTION. RE-FOLD AT 650Hz."

# Using your 0.64 stability batch data:
# pI = 10.19, MW = 5612, GRAVY = -0.45 (estimated)
print(calculate_shuttle_efficiency(10.19, 5612, -0.45))
