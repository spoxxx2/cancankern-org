import numpy as np

def run_simulation(iterations=1_000_000):
    # Sequence v3.1: GIGKFLH (7) + GS (2) + HHHHHH (6) + PPPPPA (6) + (2 padding) = 23 Residues
    total_residues = 23
    radius_initial = (total_residues * 1.5) / (2 * np.pi)
    
    print(f"[*] Initial Ring Radius (v3.1): {radius_initial:.3f} Å")
    
    # Physics: Higher stiffness (k=3.5) due to shorter GS spring
    repulsion_force = np.random.normal(loc=2.5, scale=0.5, size=iterations)
    asymmetry_torque = 1.15
    stiffness_k = 3.5 
    
    displacement = (repulsion_force * 0.85 * asymmetry_torque) / stiffness_k
    final_radii = radius_initial + displacement
    
    max_strain = (np.max(final_radii) - radius_initial) / radius_initial
    
    print("-" * 30)
    print(f"[!] PEAK RING STRAIN (v3.1): {max_strain:.2%}")
    
    if max_strain < 0.25:
        print("[STATUS] PASS: v3.1 'Tight Cinch' is STABLE.")
    else:
        print("[STATUS] FAIL: Ring still deforming. Switch to full Proline linker.")

run_simulation()
