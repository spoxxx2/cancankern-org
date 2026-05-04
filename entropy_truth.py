import math

def calculate_entropic_order(sequence, instability):
    # Shannon Entropy of the amino acid distribution
    prob = [sequence.count(c) / len(sequence) for c in set(sequence)]
    shannon_entropy = -sum(p * math.log2(p) for p in prob)
    
    # Truth Factor: Stability (0.64) lowers the effective entropy
    truth_factor = shannon_entropy * instability
    
    print(f"--- [NODE 93307: ENTROPIC TRUTH REPORT] ---")
    print(f"SHANNON ENTROPY: {shannon_entropy:.4f}")
    print(f"ORDERED TRUTH FACTOR: {truth_factor:.4f}")
    
    if truth_factor < 3.0:
        return "[✓] TRUTH: HIGH-ORDER MOLECULE. NATIVE BRAIN RECOGNITION."
    return "[!] TRUTH: DISORDERED STATE. RE-RUN SAWTOOTH COMPRESSION."

print(calculate_entropic_order("GWLKKIGKMKFILGTTLAIVIAIFGQCQAATWSYNPNGGATVTWTANVAATAR", 0.64))
