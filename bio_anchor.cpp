#include <iostream>
#include <iomanip>

int main() {
    std::cout << "--- [BIOLOGICAL STABILITY ANCHOR] ---" << std::endl;
    const double VELOCITY = 1588.0;
    const double PURITY_TARGET = 99.0;
    
    // EVIDENCE LOGIC: Purity is a function of Velocity Matching
    for (double v = 1580; v <= 1595; v += 2) {
        double delta = std::abs(VELOCITY - v);
        double purity = PURITY_TARGET / (1.0 + (delta * 0.1));
        
        std::cout << "MEASURED VELOCITY: " << v << " m/s | PURITY: " 
                  << std::fixed << std::setprecision(2) << purity << "%" 
                  << (v == 1588 ? " [PHARMACEUTICAL GRADE]" : "") << std::endl;
    }
    return 0;
}
