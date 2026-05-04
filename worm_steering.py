import numpy as np
from scipy.io import wavfile
import os

os.makedirs('INTERNAL_KEYS', exist_ok=True)

def generate_worm_steer(name, freq, wave_type):
    sr = 44100
    duration = 180 # 3 minutes
    t = np.linspace(0, duration, int(sr * duration), False)
    
    if wave_type == 'Sine':
        audio = np.sin(2 * np.pi * freq * t)
    elif wave_type == 'Sawtooth':
        audio = 2 * (t * freq - np.floor(0.5 + t * freq))
    elif wave_type == 'Square':
        audio = np.sign(np.sin(2 * np.pi * freq * t))
    
    audio = (audio * 32767).astype(np.int16)
    file_path = f"INTERNAL_KEYS/WORM_{name}_{freq}Hz.wav"
    wavfile.write(file_path, sr, audio)
    print(f"LOCKED: {file_path}")

# Synthesis Library
generate_worm_steer("REPAIR", 432.0, "Sine")
generate_worm_steer("CLOTTING", 741.0, "Sawtooth")
generate_worm_steer("ANESTHETIC", 174.0, "Square")
