import MDAnalysis as mda
from MDAnalysis.analysis import rms
import matplotlib.pyplot as plt

# Load the 24-mer trajectory
u = mda.Universe("topol.tpr", "traj_comp.xtc")
protein = u.select_atoms("protein")

# Calculate RMSF for the C-alpha atoms
R = rms.RMSF(protein.select_atoms("name CA")).run()

# Plotting the "Quantum Needle" flexibility profile
plt.plot(R.results.rmsf)
plt.xlabel("Residue Number (1-24)")
plt.ylabel("RMSF (Å)")
plt.title("24-mer Daughter Peptide: Structural Flexibility Profile")
plt.grid(True)
plt.show()
