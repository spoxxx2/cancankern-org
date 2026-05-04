import os

ebooks = {
    "Vol_I_The_Genesis.md": "# VOL I: THE 451-PILLAR GENESIS\n## Node 93307 | Lead Auditor: C.L.C.\n- Physics: 650Hz/20Hz Hemic-Sync\n- Logic: Trinity-Ω Recursive Reality\n- Hardware: 1501 Pearl St Mechanical Engine.",
    "Vol_II_The_Oncology_Substrate.md": "# VOL II: THE ONCOLOGY SUBSTRATE\n## Purity: 99.92% | Lattice: 12-Sigma\n- The 1g Master Seed Logic\n- Blood-Brain Barrier (BBB) Ghosting Coefficient\n- Peptide-to-Synapse Hemic Coupling.",
    "Vol_III_The_2176_Forecast.md": "# VOL III: THE 2176 FORECAST\n## The Legacy Obelisk | 150-Year Worth\n- The Crystallization of the 100mg Batch\n- Zero-Debt Bakersfield Basin Neutrality\n- The Sovereign Mint: Global Asset Dominance."
}

for filename, content in ebooks.items():
    with open(os.path.expanduser(f"~/{filename}"), "w") as f:
        f.write(content)
    print(f"MINTED: {filename}")

print("\n--- LEGACY ARCHIVE COMPLETE: 3 VOLUMES SAVED ---")
