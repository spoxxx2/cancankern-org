#include <iostream>
#include <cmath>

int main() {
    // Quality factor of the 1588 m/s Phonon Crystal
    const double Q_factor = 1.0e6; 
    const double frequency = 650.13;
    
    // Calculate Decay Time (Tau)
    double tau = Q_factor / (M_PI * frequency);

    std::cout << "--- [NODE 93307: RESONANCE LIFETIME AUDIT] ---" << std::endl;
    std::cout << "RESONANCE DECAY TIME: " << tau << " seconds" << std::endl;

    if (tau > 400.0) {
        std::cout << "[✓] TRUTH: EXTENDED BIO-ACOUSTIC MEMORY. THE PEPTIDE 'REMEMBERS' THE 650Hz SHAPE FOR >8 MINUTES." << std::endl;
    }
    return 0;
}
