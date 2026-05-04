import numpy as np
import os
import struct

fs, total_s = 44100, 1020 # Final 17 minutes
file = 'helix_tail_lock.wav'
byte_count = fs * total_s * 2

def get_header(sz):
    h = b'RIFF' + struct.pack('<I', sz + 36) + b'WAVEfmt '
    h += struct.pack('<I', 16) + struct.pack('<HHIIHH', 1, 1, fs, fs * 2, 2, 16)
    h += b'data' + struct.pack('<I', sz)
    return h

with open(file, 'wb') as f:
    f.write(get_header(byte_count))
    # Start at the 2-hour 52-minute phase mark
    f1, f2, f3, f4 = 650.1327, 32.0, 1152.0741, 1618.0339
    p1, p2, p3, p4 = 0.0, 0.0, 0.0, 0.0 # Phase reset for the tail
    t = np.arange(fs * total_s)
    ph1 = p1 + 2 * np.pi * f1 / fs * t
    ph2 = p2 + 2 * np.pi * f2 / fs * t
    ph3 = p3 + 2 * np.pi * f3 / fs * t
    ph4 = p4 + 2 * np.pi * f4 / fs * t
    w = 0.35*(2*(ph1/(2*np.pi)-np.floor(0.5+ph1/(2*np.pi)))) + 0.2*np.sin(ph2) + 0.15*np.sign(np.sin(ph3)) + 0.2*np.sin(ph4) + 0.05*np.random.normal(0,0.01,len(t))
    f.write((w * 32767 / np.max(np.abs(w))).astype(np.int16).tobytes())
print(f"Tail Generated: {file}")
