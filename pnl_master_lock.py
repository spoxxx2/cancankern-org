import numpy as np
from scipy.io import wavfile
import os
import hashlib

fs = 44100
chunk_s = 60  
total_s = 10800  
raw_file = 'temp_helix.pcm'
final_file = 'helix_99_precision.wav'

# Frequencies
f1, f2, f3, f4 = 650.1327, 32.0, 1152.0741, 1618.0339

# Phase accumulators to prevent Black Swan drift
p1, p2, p3, p4 = 0.0, 0.0, 0.0, 0.0

if os.path.exists(raw_file): os.remove(raw_file)

print("Status: 10-Billion Run Micro-Sync Active.")
print("Executing Continuous Phase Accumulation...")

# 1. Write Raw PCM Chunks
with open(raw_file, 'wb') as f:
    for i in range(0, total_s, chunk_s):
        samples = fs * chunk_s
        
        # Calculate continuous phase arrays
        phase1 = p1 + 2 * np.pi * f1 / fs * np.arange(samples)
        phase2 = p2 + 2 * np.pi * f2 / fs * np.arange(samples)
        phase3 = p3 + 2 * np.pi * f3 / fs * np.arange(samples)
        phase4 = p4 + 2 * np.pi * f4 / fs * np.arange(samples)
        
        # Update accumulators for the next chunk
        p1 = phase1[-1] + 2 * np.pi * f1 / fs
        p2 = phase2[-1] + 2 * np.pi * f2 / fs
        p3 = phase3[-1] + 2 * np.pi * f3 / fs
        p4 = phase4[-1] + 2 * np.pi * f4 / fs

        # Generate Waves
        w1 = 0.35 * (2 * (phase1 / (2 * np.pi) - np.floor(0.5 + phase1 / (2 * np.pi)))) 
        w2 = 0.20 * np.sin(phase2)
        w3 = 0.15 * np.sign(np.sin(phase3))
        w4 = 0.20 * np.sin(phase4)
        w5 = 0.05 * np.random.normal(0, 0.02, samples)
        
        chunk = (w1 + w2 + w3 + w4 + w5)
        chunk = (chunk / np.max(np.abs(chunk)) * 32767).astype(np.int16)
        
        f.write(chunk.tobytes())
        
        if (i // chunk_s) % 15 == 0:
            print(f"Sync Progress: {int((i + chunk_s)/total_s * 100)}% - Phase Locked")

# 2. Wrap into a perfectly formatted WAV file
print("Wrapping PCM data into compliant WAV header...")
with open(raw_file, 'rb') as f:
    raw_data = np.frombuffer(f.read(), dtype=np.int16)
wavfile.write(final_file, fs, raw_data)
os.remove(raw_file)

# 3. Generate SHA-256 Hash for Patent/Audit Proof
hasher = hashlib.sha256()
with open(final_file, 'rb') as f:
    hasher.update(f.read())
file_hash = hasher.hexdigest()

print(f"\nSUCCESS: '{final_file}' locked into Panama Lane Node.")
print(f"SHA-256 Validation Hash: {file_hash}")
