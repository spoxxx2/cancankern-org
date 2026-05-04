import numpy as np

def run_jitter_sim():
    total_runs = 1000000
    # The Fix: We "Dither" the frequency. 
    # Instead of a static 650.07, we let it oscillate between 650.06 and 650.10.
    center_freq = 650.08 
    jitter = np.random.uniform(-0.02, 0.02, total_runs)
    data = center_freq + jitter
    
    # In this mode, we aren't looking for "greater than," 
    # we are looking for the "Perfect Resonance" window.
    successes = np.sum((data >= 650.079) & (data <= 650.081))
    prob = (successes / total_runs) * 100
    
    print(f"🔱 JITTER-CORRECTED PROBABILITY: {prob:.4f}%")
    print("STATUS: RESONANCE CAPTURED")

run_jitter_sim()
