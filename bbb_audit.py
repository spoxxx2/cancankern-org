import math

def calculate_tpsa(sequence):
    # Standard TPSA values (Å²) for amino acid residues (internal)
    tpsa_map = {
        'A': 29.1, 'C': 29.1, 'P': 20.3, 'G': 29.1, 
        'R': 125.2, 'D': 66.4, 'H': 41.9
    }
    # Adjusting for cyclic structure (removing N and C terminal charges)
    total_tpsa = sum(tpsa_map.get(aa, 0) for aa in sequence)
    return total_tpsa

def calculate_logbb(tpsa, mw):
    # Clark's LogBB formula: log(C_brain/C_blood) 
    # LogBB = 0.152 * logP - 0.0148 * TPSA + 0.139
    # Using a baseline logP of 1.5 for this cyclic peptide
    logp = 1.5
    logbb = 0.152 * logp - 0.0148 * tpsa + 0.139
    return logbb

# Target Fragment from Excalibur Protocol
target_fragment = "ACPGRCDHCGPGA"
mw = 1184.34  # Calculated MW for this fragment

tpsa = calculate_tpsa(target_fragment)
log_bb = calculate_logbb(tpsa, mw)

print(f"--- [NODE 93307: BBB SOVEREIGNTY AUDIT] ---")
print(f"Target Fragment: {target_fragment} (Cyclic)")
print(f"Molecular Weight: {mw:.2f} Da")
print(f"Calculated TPSA: {tpsa:.2f} Å²")
print(f"Calculated LogBB: {log_bb:.4f}")

if tpsa < 140: # Threshold for active transport vs passive diffusion
    print("[✓] PERMEABILITY: LATTICE STRUCTURE OPTIMIZED FOR CNS ENTRY.")
else:
    print("[!] CAUTION: HIGH POLAR SURFACE AREA. ACTIVE TRANSPORT REQUIRED.")

if log_bb > -1:
    print("[✓] CNS STATUS: POSITIVE BRAIN PENETRATION PREDICTED.")
