import hashlib

# Official Sovereign Sequence & Inventor Attribution
name = "BK-Omega-7_Mother_Peptide_Inventor_Casey_Lee_Canfield"
fasta_seq = "MKWVTFISLLFLFSSAYSRGVFRRRCWCTRNCTRKCCR"

def generate_files():
    # 1. Create the .fasta file for AlphaFold/Colab
    with open("bk_omega_7.fasta", "w") as f:
        f.write(f">{name}\n{fasta_seq}\n")
    
    # 2. Generate the Sovereign Hash for Audit Trails
    seq_hash = hashlib.sha256(fasta_seq.encode()).hexdigest()
    
    print("="*65)
    print("NODE 93307: FASTA REGISTRY REBUILT")
    print(f"FILE CREATED: bk_omega_7.fasta")
    print(f"SEQUENCE HASH: {seq_hash}")
    print("="*65)

if __name__ == "__main__":
    generate_files()
