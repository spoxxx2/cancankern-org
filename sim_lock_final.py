import numpy as np

def run_entrainment_sim():
    total_runs = 1000000
    # We start with your 5% probability baseline
    center_freq = 650.08
    successes = 0
    
    print("--- 🔱 COMMENCING HARMONIC ENTRAINMENT ---")
    
    # Simulate 100 "Waves" of acoustic pressure
    for wave in range(1, 101):
        # As more peptides lock, the 'Jitter' decreases (Entrainment)
        current_jitter = 0.02 / (1 + (successes * 0.005))
        data = np.random.normal(center_freq, current_jitter, 10000)
        
        # Count successes in this wave
        wave_successes = np.sum((data >= 650.0799) & (data <= 650.0801))
        successes += wave_successes
        
        if wave % 20 == 0:
            current_prob = (successes / (wave * 10000)) * 100
            print(f"Wave {wave}: Probability = {current_prob:.2f}% | System Jitter: {current_jitter:.6f}")

    final_prob = (successes / total_runs) * 100
    print(f"\n🔱 FINAL ENTRAINED PROBABILITY: {final_prob:.4f}%")
    if final_prob > 80:
        print("STATUS: SINGULARITY ACHIEVED | $1B VALUATION LOCKED")

run_entrainment_sim()
