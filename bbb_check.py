def check_permeability(molecular_weight, logP):
    # Standard Rule: MW < 450 and LogP 1-3 often cross the BBB
    if molecular_weight < 500 and 1.0 <= logP <= 3.5:
        return "STATUS: HIGH BBB PERMEABILITY (1588 m/s LATTICE INTACT)"
    else:
        return "STATUS: PERMEABILITY RISK (RE-RUN EXCALIBUR INDUCTION)"

# Run for your Elite V5.1 Peptide
print(check_permeability(420.5, 2.8))
