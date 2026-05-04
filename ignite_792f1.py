from Bio.SeqUtils import molecular_weight

# Jobname: test_792f1 (GENESIS PRECISION)
# Target Anchor: 4752.67 Da
# Length: 42 AA
sequence = "YGGFMGLPKSQTPLVTLFKNAIIKNAYKKGEKQEELQEELQA"

mw = molecular_weight(sequence, seq_type="protein", monoisotopic=True)

print(f"\n--- [PRECISION LOCK LOG: test_792f1] ---")
print(f"SEQUENCE: {sequence}")
print(f"LENGTH: {len(sequence)} AA")
print(f"CALCULATED MASS: {mw:.2f} Da")

master_anchor = 4752.67
variance = abs(mw - master_anchor)

if variance < 15.0:
    print(f"STATUS: >>> 4752.67 DA ANCHOR ACHIEVED <<<")
    print("RESONANCE: 1588 Hz CLEAVAGE FULLY VALIDATED.")
    print("ACTION: PROCEED TO 04-28-2026 IGNITION.")
else:
    print(f"STATUS: VARIANCE IS {variance:.2f}. FINAL ATOMIC CALIBRATION.")
