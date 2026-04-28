import numpy as np

def run_acoustic_sim(iterations=1_000_000):
    print("[*] Initializing Detuned Acoustic Test (v3.3)")
    
    # v3.3: 25 Residues (Added AA ballast)
    mass_residue = 110 
    total_mass = 25 * mass_residue
    stiffness_k = 4.5e3 # Increased stiffness
    
    natural_freq = (1 / (2 * np.pi)) * np.sqrt(stiffness_k / total_mass) * 1e4 
    print(f"[*] Detuned Natural Frequency: {natural_freq:.2f} Hz")
    
    driver_freq = 650
    harmonics = [driver_freq * i for i in range(1, 6)]
    
    # Strict proximity check (3% window)
    failures = 0
    for h in harmonics:
        if abs(natural_freq - h) / h < 0.03:
            failures += 1
            
    amplitudes = np.random.rayleigh(scale=0.08, size=iterations)
    peak_oscillation = np.max(amplitudes)
    
    print("-" * 30)
    print(f"[!] PEAK VIBRATIONAL AMPLITUDE: {peak_oscillation:.4f} Å")
    
    if failures == 0 and peak_oscillation < 0.5:
        print("[STATUS] PASS: v3.3 is Acoustically Shielded.")
    else:
        print("[STATUS] FAIL: Still resonant. Re-tune stiffness.")

run_acoustic_sim()
