import numpy as np

def run_simulation(iterations=1_000_000):
    # Sequence v2.3: 27 residues with Proline Reinforcement
    total_residues = 27
    radius_initial = (total_residues * 1.5) / (2 * np.pi)
    
    print(f"[*] Initial Ring Radius (v2.3): {radius_initial:.3f} Å")
    
    # Physics: Using reinforced stiffness k=2.1 for Proline struts
    repulsion_force = np.random.normal(loc=2.5, scale=0.5, size=iterations)
    stiffness_k = 2.1 
    displacement = (repulsion_force * 0.85) / stiffness_k
    final_radii = radius_initial + displacement
    
    mean_radius = np.mean(final_radii)
    max_strain = (np.max(final_radii) - radius_initial) / radius_initial
    
    print("-" * 30)
    print(f"[!] MEAN EXPANDED RADIUS: {mean_radius:.3f} Å")
    print(f"[!] PEAK RING STRAIN: {max_strain:.2%}")
    
    if max_strain < 0.25: # Tightened threshold for high-affinity targeting
        print("[STATUS] PASS: Proline-reinforced v2.3 is STABLE.")
    else:
        print("[STATUS] FAIL: Ring still deforming. Increase Proline content.")

run_simulation()
