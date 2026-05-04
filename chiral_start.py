import numpy as np
from scipy.io.wavfile import write

fs, duration, f = 44100, 600, 1700
t = np.linspace(0, duration, fs * duration)
left, right = np.sin(2 * np.pi * f * t), np.cos(2 * np.pi * f * t)
audio = (np.vstack((left, right)).T * 32767).astype(np.int16)
write('chiral_driver.wav', fs, audio)
print("SUCCESS: 1.7 kHz Chiral Driver Generated (90° Offset).")
