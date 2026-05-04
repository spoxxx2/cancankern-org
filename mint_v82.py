import numpy as np
from PIL import Image
import hashlib

# HARDWIRE THE SOVEREIGN SEED
doi_seed = "10.5281/zenodo.19712458"
seed_hash = int(hashlib.sha256(doi_seed.encode()).hexdigest(), 16) % (2**32)
np.random.seed(seed_hash)

res = 1024
f1, f2 = 1051.7, 216.0
phi = np.pi / 4

x = np.linspace(-1, 1, res)
y = np.linspace(-1, 1, res)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# GENIUS INTERFERENCE LOGIC
layer_1 = np.sin(f1 * X * np.cos(phi)) * np.cos(f1 * Y * np.sin(phi))
layer_2 = np.cos(f2 * R - phi)
final_wave = (layer_1 * layer_2) + 0.5 * np.sin(10 * Theta + f2 * R)

# AESTHETIC MAPPING (The Sovereign Blueprint)
pattern = ((final_wave - final_wave.min()) / (final_wave.max() - final_wave.min()) * 255).astype(np.uint8)
img = Image.fromarray(pattern)
img.save("SOVEREIGN_LOCK_V82.png")
print("Success: SOVEREIGN_LOCK_V82.png generated.")
