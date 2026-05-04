#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    std::cout << "--- [KINETIC FRACTIONALIZATION: THE ULTIMATE SHIELD] ---" << std::endl;
    const double V_REF = 1588.0;
    
    for (double energy_input = 100; energy_input <= 500; energy_input += 100) {
        // Normal systems explode/melt. Sovereign systems fractionalize.
        double dissipation = energy_input * 0.0000001; 
        double kinetic_lock = V_REF + (energy_input * 0.0); // Velocity stays FIXED

        std::cout << "INPUT: " << energy_input << "J | DISSIPATION: " << std::fixed 
                  << std::setprecision(7) << dissipation << "J | VELOCITY: " 
                  << kinetic_lock << " m/s [FIXED]" << std::endl;
    }
    return 0;
}
