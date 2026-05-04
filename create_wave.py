import numpy as np
import wave
import struct

# Parameters
filename = "pulse_extraction.wav"
sample_rate = 44100
duration = 60.0  # 1 minute
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Frequencies
f1 = 44.0    # Carrier (Sine)
f2 = 528.0   # Stress (Sawtooth)
lfo = 7.83   # Pulse (Sine modulation)

# Generate Waveforms
carrier = np.sin(2 * np.pi * f1 * t)
stress = 2 * (t * f2 - np.floor(0.5 + t * f2)) # Sawtooth
modulation = (np.sin(2 * np.pi * lfo * t) + 1) / 2 # 0 to 1 range

# Composite Signal
# Layering frequencies and applying the LFO Pulse
audio = (0.5 * carrier + 0.5 * stress) * modulation

# Normalize and Convert to 16-bit PCM
audio = (audio * 32767).astype(np.int16)

# Write to WAV
with wave.open(filename, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    f.writeframes(audio.tobytes())

print(f"File '{filename}' generated successfully.")
