import numpy as np
from PIL import Image
import hashlib

# 1. ANCHOR TO DOI
doi_seed = "10.5281/zenodo.19712458"
seed_hash = int(hashlib.sha256(doi_seed.encode()).hexdigest(), 16) % (2**32)
np.random.seed(seed_hash)

# 2. FREQUENCY PARAMETERS
res = 1024
f1, f2 = 1051.7, 216.0
phi = np.pi / 3  # Adjusted phase for luxury aesthetic

x = np.linspace(-1, 1, res)
y = np.linspace(-1, 1, res)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# 3. INTERFERENCE PHYSICS
wave1 = np.sin(f1 * X) * np.cos(f1 * Y)
wave2 = np.cos(f2 * R - phi)
# The "Extraction Zone" - where waves perfectly align
combined = (wave1 * wave2) 

# 4. HYPERSPECTRAL COLOR MAPPING (The "Genius" part)
# We create 3 channels (RGB) with slightly shifted phases to simulate spectral data
r = np.sin(combined * 1.5 + 0)
g = np.sin(combined * 1.5 + (2 * np.pi / 3))
b = np.sin(combined * 1.5 + (4 * np.pi / 3))

# Normalize to 0-255
rgb_stack = np.stack([
    ((r - r.min()) / (r.max() - r.min()) * 255),
    ((g - g.min()) / (g.max() - g.min()) * 255),
    ((b - b.min()) / (b.max() - b.min()) * 255)
], axis=-1).astype(np.uint8)

img = Image.fromarray(rgb_stack)
img.save("SOVEREIGN_PRIME_LUXURY.png")
print("Handshake Success: SOVEREIGN_PRIME_LUXURY.png (Hyperspectral) generated.")
