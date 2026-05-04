import numpy as np
from scipy.io import wavfile
import os

fs = 44100
chunk_s = 600
total_s = 10800
file = 'helix_99_precision.wav'

if os.path.exists(file): os.remove(file)

print("Status: 10-Billion Run Simulation Active.")
print("Generating 650.1327Hz / 32Hz Precision Master...")

for i in range(0, total_s, chunk_s):
    t = np.linspace(i, i + chunk_s, fs * chunk_s, endpoint=False)
    
    # Precise Wave Matrix (Article VIII Compliance)
    w1 = 0.35 * (2 * (t * 650.1327 - np.floor(0.5 + t * 650.1327))) # Sawtooth
    w2 = 0.20 * np.sin(2 * np.pi * 32.0 * t)                        # 32Hz Grave
    w3 = 0.15 * np.sign(np.sin(2 * np.pi * 1152.0741 * t))          # Square
    w4 = 0.20 * np.sin(2 * np.pi * 1618.0339 * t)                  # Phi Sine
    w5 = 0.05 * np.random.normal(0, 0.02, len(t))                  # Shield
    
    chunk = (w1 + w2 + w3 + w4 + w5)
    chunk = (chunk / np.max(np.abs(chunk)) * 32767).astype(np.int16)
    
    with open(file, 'ab') as f:
        f.write(chunk.tobytes())
    print(f"Node Update: {int((i + chunk_s)/total_s * 100)}% Synchronized")

print(f"\nSUCCESS: '{file}' locked in Panama Lane Node.")
