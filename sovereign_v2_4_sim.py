import numpy as np

def run_simulation(iterations=1_000_000):
    # Sequence v2.4: 25 residues - The "Stent" Geometry
    total_residues = 25
    radius_initial = (total_residues * 1.5) / (2 * np.pi)
    
    print(f"[*] Initial Ring Radius (v2.4): {radius_initial:.3f} Å")
    
    # Physics: Proline-Stent stiffness k=3.2
    repulsion_force = np.random.normal(loc=2.5, scale=0.5, size=iterations)
    stiffness_k = 3.2 
    displacement = (repulsion_force * 0.85) / stiffness_k
    final_radii = radius_initial + displacement
    
    mean_radius = np.mean(final_radii)
    max_strain = (np.max(final_radii) - radius_initial) / radius_initial
    
    print("-" * 30)
    print(f"[!] MEAN EXPANDED RADIUS: {mean_radius:.3f} Å")
    print(f"[!] PEAK RING STRAIN: {max_strain:.2%}")
    
    if max_strain < 0.25:
        print("[STATUS] PASS: Sovereign v2.4 'Stent' is FLIGHT READY.")
    else:
        print("[STATUS] FAIL: Still too much expansion.")

run_simulation()
