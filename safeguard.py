from Bio.SeqUtils.ProtParam import ProteinAnalysis
import sys

def run_safety_check(sequence):
    try:
        # Standardize the sequence
        seq = sequence.strip().upper()
        analysis = ProteinAnalysis(seq)
        
        # Calculate key stability metrics
        pi = analysis.isoelectric_point()
        instability = analysis.instability_index()
        mw = analysis.molecular_weight()
        
        print(f"\n--- [SOVEREIGN NEURO-SAFETY REPORT] ---")
        print(f"SEQUENCE: {seq}")
        print(f"MOL. WEIGHT: {mw:.2f} Da")
        print(f"ISOELECTRIC POINT (pI): {pi:.2f}")
        print(f"INSTABILITY INDEX: {instability:.2f}")
        
        # GO/NO-GO LOGIC
        if instability > 40:
            print("\n[!] WARNING: MOLECULAR INSTABILITY DETECTED.")
            print("[!] RISK: PEPTIDE MAY DEGRADE FAST OR BECOME 'EXPLOSIVE' (LYTIC).")
            print("[!] RECOMMENDATION: RE-RUN EXCALIBUR INDUCTION @ 650Hz.")
        else:
            print("\n[✓] STATUS: DIGITALLY STABLE.")
            print("[✓] TARGET: BLOOD-BRAIN BARRIER SHUTTLE (PROCEED TO CELL ASSAY).")
            
    except Exception as e:
        print(f"ERROR: Invalid sequence. {e}")

if __name__ == "__main__":
    # If you provide a sequence in the command, use it; otherwise use default
    target_seq = sys.argv[1] if len(sys.argv) > 1 else "ACDEFGHIKLMNPQRSTVWY"
    run_safety_check(target_seq)
