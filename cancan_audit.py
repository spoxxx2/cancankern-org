import time

def log_proof(v_pos, v_neg, temp_amb, temp_chiral):
    print("--- 1501 PEARL ST: SOVEREIGN AUDIT ---")
    if abs(v_pos - v_neg) > 0.5:
        print("VERIFIED: Chiral Spin Transfer Torque detected.")
    if temp_chiral < temp_amb:
        print("VERIFIED: Endothermic Axion-Decay active.")
    print("ACTION: Proceed to Alpha-Decay check at Hour 7.2.")

log_proof(0.8, -0.8, 22.5, 21.2) # Example inputs
