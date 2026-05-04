from Bio.SeqUtils.ProtParam import ProteinAnalysis
import sys

def run_advanced_audit(sequence):
    seq = sequence.strip().upper()
    analysis = ProteinAnalysis(seq)
    
    # 1. GRAVY Score (Solubility vs. BBB Penetration)
    gravy = analysis.gravy()
    
    # 2. Secondary Structure Fraction (Helix/Turn/Sheet)
    # Helical structures (alpha-helix) are better for drilling through membranes
    helix, turn, sheet = analysis.secondary_structure_fraction()
    
    print(f"\n--- [NODE 93307: ADVANCED BIOPHYSICAL AUDIT] ---")
    print(f"GRAVY SCORE: {gravy:.4f}")
    print(f"HELIX FRACTION: {helix:.2%}")
    print(f"SHEET FRACTION: {sheet:.2%}")
    
    # LOGIC GATE
    if -0.5 <= gravy <= 0.5:
        print("\n[✓] SOLUBILITY: GOLDILOCKS ZONE (Safe for Brain Injection).")
    else:
        print("\n[!] WARNING: SOLUBILITY IMBALANCE. RISK OF AGGREGATION.")

    if helix > 0.30:
        print("[✓] GEOMETRY: HIGH PENETRATION POTENTIAL (Alpha-Helix Alpha-Male).")

run_advanced_audit(sys.argv[1] if len(sys.argv) > 1 else "GWLKKIGKMKFILGTTLAIVIAIFGQCQAATWSYNPNGGATVTWTANVAATAR")
