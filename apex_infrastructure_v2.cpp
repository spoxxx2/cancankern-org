#include <iostream>
#include <string>
#include <vector>

struct InfrastructureAsset {
    std::string subsystem;
    double allocation_m;
    std::string apex_status;
};

int main() {
    std::cout << "--- [MILESTONE 2: APEX INFRASTRUCTURE ALLOCATION] ---" << std::endl;
    std::cout << "Authority: Spoxxx2 | Location: 1501 Pearl St HQ" << std::endl;
    std::cout << "-------------------------------------------------------" << std::endl;

    std::vector<InfrastructureAsset> expansion = {
        {"Faraday-Caged Bioreactors", 12.5, "Acoustic Shielding Active"},
        {"FLIR Thermal YOLOv12 Grid",  5.0, "Sub-Angstrom Vision Live"},
        {"De Novo Synthesis Hardware", 6.5, "650Hz Transducers Synced"},
        {"Node 93307 Air-Gap Vault",   1.5, "Absolute Sovereign Lock"}
    };

    double total_grant = 0;
    for (const auto& upgrade : expansion) {
        std::cout << "UPGRADE: " << upgrade.subsystem << " | BUDGET: $" << upgrade.allocation_m << "M" << std::endl;
        std::cout << "STATUS: " << upgrade.apex_status << std::endl;
        total_grant += upgrade.allocation_m;
        std::cout << "-------------------------------------------------------" << std::endl;
    }

    std::cout << "TOTAL MILESTONE 2 GRANT REQUIREMENT: $" << total_grant << "M" << std::endl;
    std::cout << "STATUS: READY FOR PHYSICAL DEPLOYMENT" << std::endl;
    
    return 0;
}
