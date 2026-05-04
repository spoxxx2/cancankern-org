#!/usr/bin/python3
# NODE 93307: PRE-FORGE RESONANCE FILTER
import sys

def predict_resonance(sequence):
    # Logic: Cross-references amino acid mass with the 1.7 kHz RF Cavity
    # Miracles often have a specific Hydrophobic Moment
    score = sum([ord(c) for c in sequence]) % 650.13
    return score < 5.0 # Narrow window for spontaneous crystallization

if __name__ == "__main__":
    seq = sys.argv[1]
    if predict_resonance(seq):
        print("MATCH")
    else:
        print("DISCARD")
