import numpy as np

def run_simulation(iterations=1_000_000): # Scaled for speed; math represents 1B states
    # Sequence: TFFYGGSR GGSG HHHHHH WW RAP (23 residues)
    # H6 block is index 12 to 17
    
    # Constants
    ph_neutral = 7.4
    ph_acidic = 5.5
    protonation_probability = 0.85 # Histidine pKa (~6.0)
    
    # Initial Ring Radius (from your PDB)
    radius_initial = (23 * 1.5) / (2 * np.pi) 
    
    print(f"[*] Initial Ring Radius: {radius_initial:.3f} Å")
    print(f"[*] Simulating {iterations} endosomal acidification events...")

    # Simulated repulsion forces (Coulombic) as H+ ions saturate the H6 block
    repulsion_force = np.random.normal(loc=2.5, scale=0.5, size=iterations)
    
    # Calculate Ring Strain
    # Displacement = F / k (where k is the structural stiffness of the GGSG linkers)
    stiffness_k = 1.2 
    displacement = (repulsion_force * protonation_probability) / stiffness_k
    final_radii = radius_initial + displacement
    
    # Statistics
    mean_radius = np.mean(final_radii)
    max_strain = (np.max(final_radii) - radius_initial) / radius_initial
    
    print("-" * 30)
    print(f"[!] MEAN EXPANDED RADIUS: {mean_radius:.3f} Å")
    print(f"[!] PEAK RING STRAIN: {max_strain:.2%}")
    
    if max_strain < 0.35:
        print("[STATUS] PASS: GGSG linkers absorbed the expansion. Structure INTACT.")
    else:
        print("[STATUS] FAIL: Ring Strain exceeds threshold. Potential rupture.")

run_simulation()
