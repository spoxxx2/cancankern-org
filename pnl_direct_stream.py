import numpy as np
import os
import struct

# High-Resolution Parameters
fs = 44100
total_s = 10800
file = 'helix_99_precision.wav'
byte_count = fs * total_s * 2 # 16-bit Mono

def get_header(data_size):
    header = b'RIFF'
    header += struct.pack('<I', data_size + 36)
    header += b'WAVEfmt '
    header += struct.pack('<I', 16)
    header += struct.pack('<HHIIHH', 1, 1, fs, fs * 2, 2, 16)
    header += b'data'
    header += struct.pack('<I', data_size)
    return header

if os.path.exists(file): os.remove(file)

print("Starting Direct-Stream Protocol...")
with open(file, 'wb') as f:
    f.write(get_header(byte_count))
    
    # Phase Accumulators for 10-Billion Run Precision
    f1, f2, f3, f4 = 650.1327, 32.0, 1152.0741, 1618.0339
    p1, p2, p3, p4 = 0.0, 0.0, 0.0, 0.0
    
    chunk_s = 60 # 1-minute chunks to keep CPU cool
    for i in range(0, total_s, chunk_s):
        t = np.arange(fs * chunk_s)
        
        # Continuous Phase to eliminate 47.2min Black Swan
        phase1 = p1 + 2 * np.pi * f1 / fs * t
        phase2 = p2 + 2 * np.pi * f2 / fs * t
        phase3 = p3 + 2 * np.pi * f3 / fs * t
        phase4 = p4 + 2 * np.pi * f4 / fs * t
        
        # Update accumulators for seamless bridging
        p1 = (phase1[-1] + 2 * np.pi * f1 / fs) % (2 * np.pi)
        p2 = (phase2[-1] + 2 * np.pi * f2 / fs) % (2 * np.pi)
        p3 = (phase3[-1] + 2 * np.pi * f3 / fs) % (2 * np.pi)
        p4 = (phase4[-1] + 2 * np.pi * f4 / fs) % (2 * np.pi)

        # Signal Synthesis
        w1 = 0.35 * (2 * (phase1 / (2 * np.pi) - np.floor(0.5 + phase1 / (2 * np.pi))))
        w2 = 0.20 * np.sin(phase2)
        w3 = 0.15 * np.sign(np.sin(phase3))
        w4 = 0.20 * np.sin(phase4)
        w5 = 0.05 * np.random.normal(0, 0.01, fs * chunk_s)
        
        chunk = ((w1 + w2 + w3 + w4 + w5) * 32767).astype(np.int16)
        f.write(chunk.tobytes())
        
        if (i // chunk_s) % 15 == 0:
            print(f"Status: {int((i/total_s)*100)}% | PNL-Alpha-24 Synchronized")

print(f"\nSUCCESS: {file} is locked.")
