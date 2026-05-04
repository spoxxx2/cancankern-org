#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <vector>

namespace fs = std::filesystem;

int main() {
    std::string path = "CANCAN_DEBRIS_ASSETS";
    double total_methane = 0.0;
    double total_value = 0.0;
    int total_files = 0;
    int total_instances = 0;

    if (!fs::exists(path)) {
        std::cout << "📁 Vault not found. Run 'aud' first." << std::endl;
        return 1;
    }

    for (const auto& entry : fs::directory_iterator(path)) {
        if (entry.path().extension() == ".json") {
            std::ifstream file(entry.path());
            std::string line;
            while (std::getline(file, line)) {
                // Manual parsing for high-speed terminal execution without heavy libs
                if (line.find("\"mtco2e\":") != std::string::npos) {
                    total_methane += std::stod(line.substr(line.find(":") + 1));
                }
                if (line.find("\"est_recovery_value\":") != std::string::npos) {
                    total_value += std::stod(line.substr(line.find(":") + 1));
                }
                if (line.find("\"instance_count\":") != std::string::npos) {
                    total_instances += std::stoi(line.substr(line.find(":") + 1));
                }
            }
            total_files++;
        }
    }

    std::cout << "\n💎" << "===============================================" << "💎" << std::endl;
    std::cout << "       CANCAN CUMULATIVE IMPACT REPORT (C++)" << std::endl;
    std::cout << "=================================================" << std::endl;
    std::cout << "📊 TOTAL AUDITS:    " << total_files << " Assets Vaulted" << std::endl;
    std::cout << "👁️  TOTAL INSTANCES: " << total_instances << " Debris Objects" << std::endl;
    std::cout << "🌬️  METHANE SAVED:   " << total_methane << " MTCO2e Diverted" << std::endl;
    std::cout << "💰 TOTAL RECOVERY:  $" << total_value << " USD Estimated" << std::endl;
    std::cout << "⚖️  NODE AUTHORITY:  BMC 8.32.190 / Bakersfield 93307" << std::endl;
    std::cout << "=================================================" << std::endl << std::endl;

    return 0;
}
