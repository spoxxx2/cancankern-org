import numpy as np
from scipy.io import wavfile

# Precision Constants from 10-Billion Run Simulation
fs = 44100
duration = 10800  # 3 Hours
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# The Precision Five-Wave Array (650.1327 Hz + decimals)
wave1 = 0.35 * (2 * (t * 650.1327 - np.floor(0.5 + t * 650.1327))) 
wave2 = 0.25 * np.sin(2 * np.pi * 528.0159 * t)                   
wave3 = 0.15 * np.sign(np.sin(2 * np.pi * 1152.0741 * t))         
wave4 = 0.20 * np.sin(2 * np.pi * 1618.0339 * t)                 
wave5 = 0.05 * np.random.normal(0, 0.1, len(t))                  

# Composite Master
master = wave1 + wave2 + wave3 + wave4 + wave5
master = master / np.max(np.abs(master))

# Export to the Panama Lane Node directory
wavfile.write('helix_99_precision.wav', fs, (master * 32767).astype(np.int16))
print("Precision File Generated: helix_99_precision.wav")
