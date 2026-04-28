import numpy as np

def run_simulation(iterations=1_000_000):
    # Sequence v3.2: GIGKFLH (7) + PP (2) + HHHHHH (6) + PPPPPA (6) + (2 padding) = 23 Residues
    total_residues = 23
    radius_initial = (total_residues * 1.5) / (2 * np.pi)
    
    print(f"[*] Initial Ring Radius (v3.2): {radius_initial:.3f} Å")
    
    # Physics: Maximum stiffness (k=4.2) for the Full Proline Lock
    repulsion_force = np.random.normal(loc=2.5, scale=0.5, size=iterations)
    asymmetry_torque = 1.15
    stiffness_k = 4.2 
    
    displacement = (repulsion_force * 0.85 * asymmetry_torque) / stiffness_k
    final_radii = radius_initial + displacement
    
    max_strain = (np.max(final_radii) - radius_initial) / radius_initial
    
    print("-" * 30)
    print(f"[!] PEAK RING STRAIN (v3.2): {max_strain:.2%}")
    
    if max_strain < 0.25:
        print("[STATUS] PASS: v3.2 'Proline Lock' is FLIGHT READY.")
    else:
        print("[STATUS] FAIL: Physics breach. Re-evaluate earthworm motif length.")

run_simulation()
