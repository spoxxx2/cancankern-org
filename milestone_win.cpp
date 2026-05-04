#include <iostream>
#include <string>
#include <vector>

struct MilestoneAsset {
    std::string name;
    std::string tier;
    double value_m;
    std::string lock_status;
};

int main() {
    std::cout << "--- [MILESTONE 1: SOVEREIGN WIN STATE] ---" << std::endl;
    std::cout << "Authority: Spoxxx2 | Node: 93307 | April 28 Deadline" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;

    std::vector<MilestoneAsset> portfolio = {
        {"ULTIMA-ZERO", "Tier 0", 142.5, "Acoustic-Vitrified"},
        {"AETERNA-RESET", "Tier 0", 45.0, "Resonance-Locked"},
        {"ZENITH-CORE", "Tier 0", 23.3, "Sim-Sync Active"}
    };

    double total_win = 0;
    for (const auto& asset : portfolio) {
        std::cout << "ASSET: " << asset.name << " | VALUE: $" << asset.value_m << "M" << std::endl;
        std::cout << "STATUS: " << asset.lock_status << std::endl;
        total_win += asset.value_m;
        std::cout << "----------------------------------------------------" << std::endl;
    }

    std::cout << "TOTAL PORTFOLIO VALUATION: $" << total_win << "M" << std::endl;
    std::cout << "STATUS: MILESTONE 1 COMPLETE | READY FOR HANDSHAKE" << std::endl;
    return 0;
}
