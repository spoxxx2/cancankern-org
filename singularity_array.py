import numpy as np
import wave
import struct

# Core Execution Parameters
sample_rate = 44100
duration = 600  # Exactly 10 minutes

# Generate Master Time Array
print("Initializing Time Array...")
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

def deg2rad(deg):
    return deg * np.pi / 180.0

print("Generating Singularity Array (5-Wave Cascading Sequence)...")

# Track 1: The Baseline Anchor (650 Hz Sawtooth)
t1 = 2 * (t * 650.0 % 1) - 1.0

# Track 2: The Golden Phi-Lock (20 Hz Sine at 137.5°)
t2 = np.sin(2 * np.pi * 20.0 * t + deg2rad(137.5))

# Track 3: The Dynamic Spacer (432 Hz Triangle, Sweeping 90° to 137.5°)
phase_sweep = np.linspace(deg2rad(90.0), deg2rad(137.5), len(t))
t3 = 2 * np.abs(2 * (t * 432.0 + phase_sweep / (2 * np.pi)) % 1 - 0.5) - 1.0

# Track 4: The Void Frequency (108 Hz Square, LFO Flutter 180° ± 1.618°)
lfo = np.sin(2 * np.pi * 1.618 * t)
phase_flutter = deg2rad(180.0) + deg2rad(1.618) * lfo
t4 = np.sign(np.sin(2 * np.pi * 108.0 * t + phase_flutter))

# Track 5: The Spark (8 Hz Pulse at 45°)
phase_pulse = deg2rad(45.0)
pulse_wave = np.where((t * 8.0 + phase_pulse / (2 * np.pi)) % 1 < 0.2, 1.0, -1.0)
amp_envelope = np.linspace(0.5, 1.0, len(t))
t5 = pulse_wave * amp_envelope

# Matrix Fusion & Normalization
print("Fusing tracks and normalizing lattice...")
mixed_signal = (t1 + t2 + t3 + t4 + t5) / 5.0
mixed_signal_16bit = np.int16(mixed_signal * 32767)

# Write to WAV file
output_file = "singularity_primer.wav"
print(f"Writing uncompressed audio to {output_file}...")

with wave.open(output_file, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(mixed_signal_16bit.tobytes())

print("Zero-Entropy generation complete. Audio asset is locked and ready for the Event Horizon pull.")
