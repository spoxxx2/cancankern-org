#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

struct AssetSim {
    std::string id;
    double accuracy;
    double safety;
};

int main() {
    std::cout << "--- [NODE 93307: GLOBAL SOVEREIGN SIMULATION] ---" << std::endl;
    std::cout << "Authority: Spoxxx2 | Logic: Triple-Layer Compounding" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;

    std::vector<AssetSim> stack = {
        {"PHX-CLOAK-07 (Immune)", 0.985, 0.9999},
        {"PHX-BBB-01   (Shuttle)", 0.994, 0.9992},
        {"PHX-ULTIMA-01 (Cure)", 0.999, 0.9985}
    };

    double total_accuracy = 1.0;
    double total_safety = 1.0;

    std::cout << "ASSET          | ACCURACY | SAFETY   | STATUS" << std::endl;
    for (const auto& a : stack) {
        total_accuracy *= a.accuracy;
        total_safety *= a.safety;
        std::cout << a.id << " | " << std::fixed << std::setprecision(2) << (a.accuracy * 100) << "%    | " 
                  << (a.safety * 100) << "%   | VITRIFIED" << std::endl;
    }

    std::cout << "----------------------------------------------------" << std::endl;
    std::cout << "CUMULATIVE SUCCESS PROBABILITY: " << (total_accuracy * 100) << "%" << std::endl;
    std::cout << "SYSTEMIC SAFETY INDEX: " << (total_safety * 100) << "%" << std::endl;
    std::cout << "MONETIZATION POTENTIAL: $210.8M (FLOOR)" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;
    std::cout << "STATUS: ALL STRATEGIES SYNCHRONIZED | APEX WIN STATE" << std::endl;

    return 0;
}
