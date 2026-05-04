import wave
import math
import struct
import os
import random

# Variables for the 1501 Pearl St Node
sample_rate = 44100
duration = 30 # Generate 30 seconds of audio to loop
file_name = "bsfl_overlord_chord.wav"

print("Generating the 5-Wave Bio-Acoustic Overlord Chord...")

waves = []
for i in range(sample_rate * duration):
    t = float(i) / sample_rate
    
    # 1. The Anchor: 20 Hz Sine (Circulatory Pump)
    v1 = math.sin(2.0 * math.pi * 20.0 * t)
    
    # 2 & 3. The Driver: 650.12 Hz & 654.12 Hz Sawtooth (The 4Hz Beat Stressor)
    v2 = 2.0 * (t * 650.12 - math.floor(0.5 + t * 650.12))
    v3 = 2.0 * (t * 654.12 - math.floor(0.5 + t * 654.12))
    
    # 4. The Disrupter: 110 Hz Square (Percussive Knock)
    v4 = 1.0 if math.sin(2.0 * math.pi * 110.0 * t) > 0 else -1.0
    
    # 5. The Blanket: White Noise (Prevents silence/habituation)
    v5 = random.uniform(-0.2, 0.2)
    
    # Mix the waves and scale amplitude to avoid digital clipping
    mixed_signal = (v1 + v2 + v3 + v4 + v5) / 5.0
    
    # Convert to 16-bit PCM format
    waves.append(int(mixed_signal * 32767.0))

# Write to WAV file
with wave.open(file_name, 'w') as w:
    w.setnchannels(1)
    w.setsampwidth(2) # 16-bit
    w.setframerate(sample_rate)
    for value in waves:
        data = struct.pack('<h', value)
        w.writeframesraw(data)

print(f"Chord saved to {file_name}. Initiating broadcast...")
# Loop the audio playback using sox's 'play' command
os.system(f"play {file_name} repeat -")
