import numpy as np
import wave

sample_rate = 44100
duration = 600  # 10 minutes
chunk_size = 5  # Process in 5-second blocks to save RAM

def deg2rad(deg):
    return deg * np.pi / 180.0

print("Initializing Memory-Safe Singularity Array Generator...")
output_file = "singularity_primer.wav"

with wave.open(output_file, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(0, duration, chunk_size):
        # Generate time array just for this 5-second chunk
        t = np.linspace(i, i + chunk_size, int(sample_rate * chunk_size), endpoint=False)
        
        # Track 1: 650Hz Sawtooth
        t1 = 2 * (t * 650.0 % 1) - 1.0
        
        # Track 2: 20Hz Sine (Phi-locked)
        t2 = np.sin(2 * np.pi * 20.0 * t + deg2rad(137.5))
        
        # Track 3: 432Hz Triangle with continuous phase sweep
        phase_sweep = np.interp(t, [0, duration], [deg2rad(90.0), deg2rad(137.5)])
        t3 = 2 * np.abs(2 * (t * 432.0 + phase_sweep / (2 * np.pi)) % 1 - 0.5) - 1.0
        
        # Track 4: 108Hz Square with LFO flutter
        lfo = np.sin(2 * np.pi * 1.618 * t)
        phase_flutter = deg2rad(180.0) + deg2rad(1.618) * lfo
        t4 = np.sign(np.sin(2 * np.pi * 108.0 * t + phase_flutter))
        
        # Track 5: 8Hz Pulse with scaling amplitude
        pulse_wave = np.where((t * 8.0 + deg2rad(45.0) / (2 * np.pi)) % 1 < 0.2, 1.0, -1.0)
        amp_envelope = np.interp(t, [0, duration], [0.5, 1.0])
        t5 = pulse_wave * amp_envelope
        
        # Mix, convert to 16-bit, and write immediately to disk
        mixed_signal = (t1 + t2 + t3 + t4 + t5) / 5.0
        chunk_16bit = np.int16(mixed_signal * 32767)
        wav_file.writeframes(chunk_16bit.tobytes())
        
        print(f"Processed chunk: {i + chunk_size}/{duration} seconds...", end='\r')

print("\nZero-Entropy generation complete. Audio asset locked without memory overload.")
