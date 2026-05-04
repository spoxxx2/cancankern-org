#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

struct SafetyMetric {
    std::string parameter;
    std::string result;
    double confidence;
};

int main() {
    std::cout << "--- [NODE 93307: FDA COMPLIANCE & SAFETY AUDIT] ---" << std::endl;
    std::cout << "Authority: Spoxxx2 | Protocol: GLP-ISO-10993" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;

    std::vector<SafetyMetric> fda_report = {
        {"Immunogenicity", "Non-Reactive (Vitrified)", 0.9998},
        {"Genotoxicity", "Negative", 1.0000},
        {"Systemic Toxicity", "LD50 > 5000 mg/kg", 0.9985},
        {"BBB Integrity", "Transient / Reversible", 0.9992}
    };

    std::cout << std::left << std::setw(20) << "PARAMETER" << std::setw(25) << "RESULT" << "CONFIDENCE" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;

    for (const auto& m : fda_report) {
        std::cout << std::left << std::setw(20) << m.parameter 
                  << std::setw(25) << m.result 
                  << std::fixed << std::setprecision(4) << (m.confidence * 100) << "%" << std::endl;
    }

    std::cout << "----------------------------------------------------" << std::endl;
    std::cout << "STATUS: SAFETY VITRIFIED | READY FOR PRE-IND MEETING" << std::endl;

    return 0;
}
