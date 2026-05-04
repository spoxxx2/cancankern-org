import polars as pl
import os

# The "Sovereign 25" Manifest
species = ["BSFL_Gen2", "Mamba_Delta", "Conan_Repair", "Tardigrade_Space", "Olavius_Algar"]

for s in species:
    print(f"\n[STAGING] FORGING GODLY PEPTIDE FOR: {s}")
    
    # 1. ACTUAL FORGE: Run LAMMPS first
    # This creates the {s}_GODLY.log file the script needs
    os.system(f"export OMP_NUM_THREADS=4 && lmp -in in.godly -var spec {s} -log {s}_GODLY.log")
    
    # 2. SCAN: Look for the 0.95 Curvature 'Godly' Heart
    try:
        if os.path.exists(f"{s}_GODLY.log"):
            df = pl.scan_csv(f"{s}_GODLY.log", separator=" ", ignore_errors=True)
            godly_hit = df.filter(pl.col("curvature") > 0.95).collect()
            
            if not godly_hit.is_empty():
                print(f"!!! SUCCESS: GODLY PEPTIDE FOUND IN {s} !!!")
                godly_hit.write_csv(f"forensic_outputs/{s}_GODLY_COA.csv")
            else:
                print(f"[STATUS] {s}: Simulation complete. No 'Godly' signature.")
        else:
            print(f"[ERROR] {s}: Log file was not generated.")
    except Exception as e:
        print(f"[ERROR] Could not process {s}: {e}")

print("\n--- 10-BILLION RUN COMPLETE ---")
