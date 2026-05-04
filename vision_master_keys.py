import numpy as np
from scipy.io import wavfile
import os

os.makedirs('INTERNAL_KEYS', exist_ok=True)

def generate_sovereign_key(name, freq, wave_type, duration=180):
    sr = 44100
    t = np.linspace(0, duration, int(sr * duration), False)
    
    if wave_type == 'Sawtooth':
        audio = 2 * (t * freq - np.floor(0.5 + t * freq))
    elif wave_type == 'Square':
        audio = np.sign(np.sin(2 * np.pi * freq * t))
    elif wave_type == 'Sine':
        audio = np.sin(2 * np.pi * freq * t)
    
    audio = (audio * 32767).astype(np.int16)
    file_path = f"INTERNAL_KEYS/{name}_{freq}Hz_{wave_type}.wav"
    wavfile.write(file_path, sr, audio)
    print(f"LOCKED: {file_path}")

keys = [
    ("MARG42_ONCOLOGY", 1588.0, "Sawtooth"),
    ("BBB_ALPHA_7", 1588.0, "Sawtooth"),
    ("ARA290_PAIN", 1442.0, "Square"),
    ("SEL933_EUPHORIA", 650.0, "Sine"),
    ("MOTSc_ENERGY", 852.0, "Sine"),
    ("BPC157_REPAIR", 528.0, "Sine")
]

for name, freq, wave in keys:
    generate_sovereign_key(name, freq, wave)
