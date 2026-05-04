#include <iostream>
#include <iomanip>

int main() {
    std::cout << "--- [FDA CGMP: SOLVENT TEMPERATURE STABILITY] ---" << std::endl;
    const double OPTIMAL_TEMP = -15.0; // Chilled Acetone Target (°C)
    
    for (double temp = -20.0; temp <= 0.0; temp += 5.0) {
        // Higher temps lead to peptide degradation (loss of purity)
        double degradation_risk = (temp > -10.0) ? (temp + 10.0) * 0.05 : 0.0001;
        double potency = 100.0 * (1.0 - degradation_risk);

        std::cout << "SOLVENT TEMP: " << std::fixed << std::setprecision(1) << temp 
                  << "°C | PEPTIDE POTENCY: " << std::setprecision(4) << potency 
                  << "% | " << (temp <= -10.0 ? "CGMP VALID" : "RISK DETECTED") << std::endl;
    }
    return 0;
}
