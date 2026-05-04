import numpy as np
import wave

# Parameters
fn = "jar_extraction.wav"
sr = 44100
dur = 60.0 
t = np.linspace(0, dur, int(sr * dur), endpoint=False)

# Frequencies
f_carrier = 52.0    # Hydro-Seismic Carrier
f_stress = 528.0    # Bio-Acoustic Agitator
f_pulse = 10.0      # Modulation

# Signal Construction
carrier = np.sign(np.sin(2 * np.pi * f_carrier * t)) # Square wave
stress = 2 * (t * f_stress - np.floor(0.5 + t * f_stress)) # Sawtooth
pulse = (np.sin(2 * np.pi * f_pulse * t) + 1) / 2 # Pulse

# Combine and Normalize
audio = (0.6 * carrier + 0.4 * stress) * pulse
audio = (audio * 32767).astype(np.int16)

with wave.open(fn, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sr)
    f.writeframes(audio.tobytes())

print(f"Extraction file '{fn}' is ready for the Panama Lane node.")
