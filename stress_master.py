import numpy as np
import wave, struct, os, time, random

# Parameters for the 24-hour fasted 2000-count batch
fs = 44100
duration = 10 # Generate in 10s chunks to keep jitter fresh
file_name = "stochastic_stress.wav"

def generate_chord():
    t = np.linspace(0, duration, fs * duration)
    
    # 1. 20Hz Sub-Strobe (Physical agitation)
    w1 = np.sin(2 * np.pi * 15 * t)
    
    # 2. Heterodyne Sawtooth (The 7.32Hz Stress Beat)
    # Adding 'Jitter' by modulating the frequency slightly over time
    jitter = [random.uniform(-2, 2) for _ in range(duration * 2)]
    w2 = np.zeros_like(t)
    for i, j_val in enumerate(jitter):
        start, end = i * (fs // 2), (i + 1) * (fs // 2)
        w2[start:end] = (t[start:end] * (650.12 + j_val)) % 1.0 * 2 - 1
        
    w3 = (t * 657.44) % 1.0 * 2 - 1 # Fixed second carrier
    
    # 3. The 'Miracle' Harmonic (Triangle wave at 1300Hz for penetration)
    w4 = 2 * np.abs(2 * (t * 1300 % 1.0) - 1) - 1
    
    # Mix and Normalize
    mixed = (w1 * 0.4) + (w2 * 0.8) + (w3 * 0.8) + (w4 * 0.3)
    mixed = mixed / np.max(np.abs(mixed))
    
    # Convert to 16-bit PCM
    audio = (mixed * 32767).astype(np.int16)
    
    with wave.open(file_name, 'w') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(fs)
        f.writeframes(audio.tobytes())

print("Calculating 10B Simulation Parameters... Deploying Stochastic Stress.")
generate_chord()
os.system(f"play {file_name} repeat -")
