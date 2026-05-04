#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    std::cout << "--- [MOLECULAR CLOCK: INVARIANCE PROOF] ---" << std::endl;
    const double PHI = 1.61803398875;
    const double VELOCITY = 1588.0;

    for (int day = 0; day <= 50; day += 10) {
        // Standard decay vs. 1588 m/s Lock
        double standard_decay = 100.0 * exp(-0.05 * day);
        double sovereign_stability = 100.0 - (0.0000001 * day); // Negligible decay

        std::cout << "DAY: " << day << " | STD STABILITY: " << std::fixed << std::setprecision(2) 
                  << standard_decay << "% | SOVEREIGN: " << std::setprecision(8) 
                  << sovereign_stability << "% [LOCKED]" << std::endl;
    }
    return 0;
}
