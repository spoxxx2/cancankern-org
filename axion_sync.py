import numpy as np
from scipy.io.wavfile import write

fs, duration = 44100, 3600 # 1 Hour Pulse
t = np.linspace(0, duration, fs * duration)
# 1.7 kHz Chiral Pump + 10.2 kHz Axion Anchor
chiral = np.sin(2 * np.pi * 1700 * t) + 0.1 * np.sin(2 * np.pi * 10200 * t)
write('axion_harvest.wav', fs, (chiral * 32767).astype(np.int16))
