import numpy as np

# Parameters for your 8.88 kDa "Daughter"
sims = 1000000 
res = 1800 # Target TEER
flux = 0.05 # Theoretical permeability

def simulate():
    noise = np.random.normal(0, 0.01, sims)
    success = np.mean((flux / (res / 1000)) + noise > 0.1)
    return success

result = simulate()
print(f"\n[NODE 1501 AUDIT]")
print(f"Asset: 8.88 kDa Daughter Peptide")
print(f"BBB Crossing Probability: {result * 100:.2f}%")
