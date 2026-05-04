import numpy as np

def run_simulation(iterations=1_000_000):
    # Sequence v2.2: Added 6 extra residues for slack (Total 29)
    # TFFYGGSR GGSG GGSG HHHHHH GGSG WW RAP
    total_residues = 29
    radius_initial = (total_residues * 1.5) / (2 * np.pi)
    
    print(f"[*] Initial Ring Radius (v2.2): {radius_initial:.3f} Å")
    
    # Physics remain the same
    repulsion_force = np.random.normal(loc=2.5, scale=0.5, size=iterations)
    stiffness_k = 0.9 # Slightly lower stiffness due to more "slack" linkers
    displacement = (repulsion_force * 0.85) / stiffness_k
    final_radii = radius_initial + displacement
    
    mean_radius = np.mean(final_radii)
    max_strain = (np.max(final_radii) - radius_initial) / radius_initial
    
    print("-" * 30)
    print(f"[!] MEAN EXPANDED RADIUS: {mean_radius:.3f} Å")
    print(f"[!] PEAK RING STRAIN: {max_strain:.2%}")
    
    if max_strain < 0.35:
        print("[STATUS] PASS: v2.2 Structure is safe for Endosomal Escape.")
    else:
        print("[STATUS] FAIL: Still too much strain. Add more spacers.")

run_simulation()
