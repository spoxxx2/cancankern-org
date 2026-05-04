import math

def generate_pdb(sequence, filename="sovereign_v2.pdb"):
    # Standard amino acid backbone atom offsets (simplified for simulation)
    atoms = ["N", "CA", "C", "O"]
    coords = []
    
    # Simple alpha-helix-like projection for Digital Twin validation
    for i, amino in enumerate(sequence):
        phi = i * 0.8  # Simulated spiral
        x = 1.5 * math.cos(phi)
        y = 1.5 * math.sin(phi)
        z = i * 1.5
        
        for j, atom in enumerate(atoms):
            coords.append({
                "serial": len(coords) + 1,
                "name": atom,
                "res_name": "TRP" if amino == "W" else "HIS" if amino == "H" else "ALA",
                "chain": "A",
                "res_seq": i + 1,
                "x": x + (j * 0.5),
                "y": y + (j * 0.2),
                "z": z + (j * 0.3)
            })

    with open(filename, "w") as f:
        for c in coords:
            f.write(f"ATOM  {c['serial']:5d} {c['name']:^4s} {c['res_name']:3s} {c['chain']}{c['res_seq']:4d}    {c['x']:8.3f}{c['y']:8.3f}{c['z']:8.3f}  1.00  0.00           {c['name'][0]}\n")
        f.write("END\n")
    print(f"[*] SUCCESS: {filename} generated at {z:.2f} Angstroms.")

# The RMT-PH Sovereign Sequence (v2.0)
generate_pdb("TFFYGGSRGGSGHHHHHHWWRAP")
