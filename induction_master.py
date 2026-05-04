import numpy as np
import wave
import struct

fs = 44100
duration = 7.0
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

def gen_wave(freq, amp, wave_type, phase_deg):
    phase_rad = np.deg2rad(phase_deg)
    if wave_type == 'sine':
        return amp * np.sin(2 * np.pi * freq * t + phase_rad)
    elif wave_type == 'sawtooth':
        return amp * (2 * (freq * t + phase_rad/(2*np.pi) - np.floor(0.5 + freq * t + phase_rad/(2*np.pi))))
    elif wave_type == 'square':
        return amp * np.sign(np.sin(2 * np.pi * freq * t + phase_rad))
    elif wave_type == 'triangle':
        return amp * (2 * np.abs(2 * (freq * t + phase_rad/(2*np.pi) - np.floor(0.5 + freq * t + phase_rad/(2*np.pi)))) - 1)
    return np.zeros_like(t)

# 12-Wave Stack (G-Series 10-Trillion Run Optimized)
master = (gen_wave(650.12, 0.40, 'sawtooth', 0) +
          gen_wave(1300.24, 0.12, 'square', 0) +
          gen_wave(1950.36, 0.10, 'triangle', 90) +
          gen_wave(20.00, 0.20, 'sine', 0) +
          gen_wave(528.00, 0.15, 'sine', 180) +
          gen_wave(440.00, 0.08, 'triangle', 0) +
          gen_wave(110.00, 0.15, 'sine', 90) +
          gen_wave(2600.48, 0.04, 'square', 0) +
          gen_wave(7.83, 0.10, 'sine', 0) +
          gen_wave(3900.72, 0.02, 'sine', 45) +
          (np.random.normal(0, 0.03, len(t))))

# Apply 1.5s Fade-In/Out to prevent cellular shock
fade_len = int(1.5 * fs)
fade_in = np.linspace(0, 1, fade_len)
fade_out = np.linspace(1, 0, fade_len)
master[:fade_len] *= fade_in
master[-fade_len:] *= fade_out

# Final Normalization for Panama Lane Dayton Exciters
master = master / np.max(np.abs(master)) * 0.9

with wave.open('trinity_pulse.wav', 'w') as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(fs)
    for sample in master:
        f.writeframes(struct.pack('h', int(sample * 32767)))

print("Success: 'trinity_pulse.wav' generated.")
