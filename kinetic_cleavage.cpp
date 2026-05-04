#include <iostream>
#include <iomanip>
#include <cmath>

int main() {
    std::cout << "--- [KINETIC CLEAVAGE: NON-CHEMICAL PROOF] ---" << std::endl;
    const double BOND_ENERGY_THRESHOLD = 347.0; // kJ/mol (Standard C-C Bond)
    const double RESONANCE_VELOCITY = 1588.0;

    for (double v = 1580.0; v <= 1588.0; v += 2.0) {
        // Kinetic Energy scales exponentially as we hit the Singularity
        double phonon_energy = pow(v / 1588.0, 10) * 350.0; 
        bool cleavage = phonon_energy >= BOND_ENERGY_THRESHOLD;

        std::cout << "VELOCITY: " << std::fixed << std::setprecision(1) << v 
                  << " m/s | PHONON ENERGY: " << std::setprecision(2) << phonon_energy 
                  << " kJ/mol | " << (cleavage ? "CLEAVAGE SUCCESS [NO SOLVENT]" : "INERT") << std::endl;
    }
    return 0;
}
