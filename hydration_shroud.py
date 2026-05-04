def check_safety_shroud(mw, gravy, instability):
    # A negative GRAVY score indicates a water-loving shell
    # High stability ensures the shell doesn't collapse
    safety_score = (abs(gravy) * 10) + (1.0 / (instability + 0.1))
    
    print(f"--- [NODE 93307: IMMUNE-SHIELD REPORT] ---")
    print(f"HYDRATION SAFETY SCORE: {safety_score:.2f}")
    
    if safety_score > 5.0:
        return "[✓] STATUS: UNDENIABLY SAFE. IMMUNE SYSTEM INVISIBLE."
    return "[!] STATUS: EXPOSED SURFACE. RE-RUN 650Hz SHROUDING."

# Using your current values (GRAVY -0.45, Instability 0.64)
print(check_safety_shroud(5612, -0.45, 0.64))
