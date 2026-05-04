import numpy as np

def run_simulation(iterations=1_000_000):
    # Sequence v3.0: GIGKFLH (Earthworm) + GGSG + H6 + P5A (25 residues)
    total_residues = 25
    radius_initial = (total_residues * 1.5) / (2 * np.pi)
    
    # Asymmetry Factor: GIGKFLH is bulkier than the original TFFYGGSR
    asymmetry_torque = 1.15 
    
    print(f"[*] Initial Ring Radius (v3.0): {radius_initial:.3f} Å")
    
    # Physics: Stent stiffness k=3.2, but with Torque applied
    repulsion_force = np.random.normal(loc=2.5, scale=0.5, size=iterations)
    stiffness_k = 3.2 
    
    # Displacement with Asymmetry modifier
    displacement = (repulsion_force * 0.85 * asymmetry_torque) / stiffness_k
    final_radii = radius_initial + displacement
    
    max_strain = (np.max(final_radii) - radius_initial) / radius_initial
    
    print("-" * 30)
    print(f"[!] PEAK RING STRAIN (v3.0): {max_strain:.2%}")
    
    if max_strain < 0.25:
        print("[STATUS] PASS: Earthworm Graft is stable within the Stent.")
    else:
        print("[STATUS] FAIL: Earthworm motif causing excessive torque. Shorten the GGSG spring.")

run_simulation()
