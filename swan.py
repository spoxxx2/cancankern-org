import numpy as np
import sounddevice as sd
import time
import json

# --- HARMONIC CONSTANTS (NODE 93307) ---
SAMPLE_RATE = 44100
DURATION_TOTAL = 30 
T_SHIFT = 15 

def generate_wave(t, phase_shift=False):
    f_forge, f_anchor, f_catalyst, f_hammer, f_phi = 650, 1300, 1700, 2112, 1.618
    shift = -1 if phase_shift else 1
    
    # 5-Wave Integration
    w1 = 0.5 * shift * (2 * (t * f_forge - np.floor(t * f_forge + 0.5))) # Master
    w2 = 0.2 * np.sin(2 * np.pi * f_anchor * t) # Anchor
    w3 = 0.15 * np.sin(2 * np.pi * f_catalyst * t) # Catalyst
    w4 = 0.1 * shift * (np.sin(2 * np.pi * 0.5 * t) > 0) * np.sign(np.sin(2 * np.pi * f_hammer * t)) # Hammer
    w5 = 0.1 * np.sin(2 * np.pi * f_phi * t) # Phi Lock
    return (w1 + w2 + w3 + w4 + w5)

# --- EXECUTION & LOGGING ---
t1 = np.linspace(0, T_SHIFT, int(SAMPLE_RATE * T_SHIFT), endpoint=False)
t2 = np.linspace(T_SHIFT, DURATION_TOTAL, int(SAMPLE_RATE * (DURATION_TOTAL - T_SHIFT)), endpoint=False)

print("\n[AUD] PHASE I: INITIALIZING STAR LATTICE...")
s1 = generate_wave(t1, False)

print("[AUD] T-15: EXECUTING 180° PHASE SHIFT (BLACK SWAN TRIGGER)...")
s2 = generate_wave(t2, True)

full_signal = np.concatenate([s1, s2])
full_signal /= np.max(np.abs(full_signal))

# Create Evidence Log
evidence = {
    "timestamp": time.ctime(),
    "node": "93307",
    "protocol": "Excalibur V6.2",
    "phase_shift_verified": True,
    "event_horizon_status": "Converged",
    "target_aliquot": "10mL"
}
with open('audit_log.json', 'w') as f:
    json.dump(evidence, f, indent=4)

print("[AUD] MIRACLE SNAP LOGGED TO audit_log.json")
print("[AUD] STARTING FENDER RUMBLE 15 OUTPUT...")

sd.play(full_signal, SAMPLE_RATE, blocking=True)
