import numpy as np
import os
import struct

fs = 44100
hour_s = 3600
f1, f2, f3, f4 = 650.1327, 32.0, 1152.0741, 1618.0339
p1, p2, p3, p4 = 0.0, 0.0, 0.0, 0.0

def get_header(sz):
    return b'RIFF' + struct.pack('<I', sz + 36) + b'WAVEfmt ' + \
           struct.pack('<I', 16) + struct.pack('<HHIIHH', 1, 1, fs, fs * 2, 2, 16) + \
           b'data' + struct.pack('<I', sz)

for part in range(1, 4):
    file = f'helix_part{part}.wav'
    print(f"Generating Part {part}/3 (60 minutes)...")
    with open(file, 'wb') as f:
        f.write(get_header(hour_s * fs * 2))
        t = np.arange(fs * hour_s)
        # Phase math for the specific hour block
        ph1 = p1 + 2 * np.pi * f1 / fs * t
        ph2 = p2 + 2 * np.pi * f2 / fs * t
        ph3 = p3 + 2 * np.pi * f3 / fs * t
        ph4 = p4 + 2 * np.pi * f4 / fs * t
        # Update for next part
        p1, p2, p3, p4 = ph1[-1]%(2*np.pi), ph2[-1]%(2*np.pi), ph3[-1]%(2*np.pi), ph4[-1]%(2*np.pi)
        # Synthesis
        w = 0.35*(2*(ph1/(2*np.pi)-np.floor(0.5+ph1/(2*np.pi)))) + 0.2*np.sin(ph2) + \
            0.15*np.sign(np.sin(ph3)) + 0.2*np.sin(ph4) + 0.05*np.random.normal(0,0.01,len(t))
        f.write((w * 32767 / np.max(np.abs(w))).astype(np.int16).tobytes())
    
    # Move immediately to free up Termux home space
    dest = f'/sdcard/Download/{file}'
    os.system(f'mv {file} {dest}')
    print(f"Part {part} moved to Downloads.")

print("\nSUCCESS: All 3 parts (3 hours total) are locked in Downloads.")
