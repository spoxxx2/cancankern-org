import numpy as np
import os
import struct

fs, total_s = 44100, 10800
file = 'helix_99_precision.wav'
byte_count = fs * total_s * 2

def get_header(sz):
    h = b'RIFF' + struct.pack('<I', sz + 36) + b'WAVEfmt '
    h += struct.pack('<I', 16) + struct.pack('<HHIIHH', 1, 1, fs, fs * 2, 2, 16)
    h += b'data' + struct.pack('<I', sz)
    return h

print("Critical Phase: Generating 3-Hour Precision Master...")
with open(file, 'wb') as f:
    f.write(get_header(byte_count))
    f1, f2, f3, f4 = 650.1327, 32.0, 1152.0741, 1618.0339
    p1, p2, p3, p4 = 0.0, 0.0, 0.0, 0.0
    chunk_s = 60 
    for i in range(0, total_s, chunk_s):
        t = np.arange(fs * chunk_s)
        ph1 = p1 + 2 * np.pi * f1 / fs * t
        ph2 = p2 + 2 * np.pi * f2 / fs * t
        ph3 = p3 + 2 * np.pi * f3 / fs * t
        ph4 = p4 + 2 * np.pi * f4 / fs * t
        p1, p2, p3, p4 = ph1[-1]%(2*np.pi), ph2[-1]%(2*np.pi), ph3[-1]%(2*np.pi), ph4[-1]%(2*np.pi)
        w = 0.35*(2*(ph1/(2*np.pi)-np.floor(0.5+ph1/(2*np.pi)))) + 0.2*np.sin(ph2) + 0.15*np.sign(np.sin(ph3)) + 0.2*np.sin(ph4) + 0.05*np.random.normal(0,0.01,fs*chunk_s)
        f.write((w * 32767 / np.max(np.abs(w))).astype(np.int16).tobytes())
        if (i // chunk_s) % 20 == 0: print(f"Progress: {int((i/total_s)*100)}% | Phase Locked")
print(f"\nSUCCESS: {file} is locked.")
