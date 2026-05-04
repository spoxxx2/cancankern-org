#include <iostream>

int main() {
    double f1 = 440.0;
    double f2 = 2220.0;
    double phi = 1.618033;

    std::cout << "\n--- CANCAN HARMONIC RESONANCE SCANNER ---" << std::endl;
    for (int n = 1; n <= 5; ++n) {
        std::cout << "Harmonic " << n << " | Align: " << f1 * n << "Hz | Strike: " << f2 * n << "Hz" << std::endl;
    }
    std::cout << "-----------------------------------------" << std::endl;
    std::cout << "BLACK SWAN HORIZON (Phi-Lock): " << f2 * phi << " Hz" << std::endl;
    std::cout << "-----------------------------------------\n" << std::endl;
    return 0;
}
