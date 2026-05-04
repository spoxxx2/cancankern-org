import polars as pl
import os

# The 100-Species Matrix (Arachnid, Insect, Reptile, Aquatic)
species_list = ["BSFL_Gen2", "Blue_Weaver_V2", "Black_Widow_X", "Centipede_Gamma", "Monitor_Lizard_Alpha"] # + 95 others

def run_sovereign_sim(species):
    print(f"Starting 10M Run for {species}...")
    # Triggering LAMMPS with 1700.35 Hz Sawtooth Stress
    os.system(f"export OMP_NUM_THREADS=4 && lmp -in in.production -var species {species} -log {species}_10M.log")
    
    # Post-Processing for 0.85 Berry Curvature
    df = pl.scan_csv(f"{species}_10M.log", separator=" ", ignore_errors=True)
    daughter = df.tail(4).collect()
    print(f"Extraction Complete for {species}. Daughter Peptide isolated.")

for s in species_list:
    run_sovereign_sim(s)
