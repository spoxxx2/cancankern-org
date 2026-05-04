#include <iostream>

int main() {
    const double molarity = 0.290; // 290 mOsm/L (Human Physiological Standard)
    const double r_constant = 0.0821; 
    const double temp_k = 310.15; // 37 C
    
    // Calculate Osmotic Pressure (Pi = iMRT)
    double pressure = 1.0 * molarity * r_constant * temp_k;

    std::cout << "--- [NODE 93307: OSMOTIC PRESSURE AUDIT] ---" << std::endl;
    std::cout << "PRESSURE: " << pressure << " atm" << std::endl;

    if (pressure > 7.0 && pressure < 7.5) {
        std::cout << "[✓] TRUTH: ISOTONIC HARMONY. ZERO TISSUE STRESS DETECTED." << std::endl;
    }
    return 0;
}
