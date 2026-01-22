#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream log("audit_success.log");
    std::string line;
    int total_assets = 0;
    const int MILESTONE = 12; // ~10k Value (12 assets * 40)

    while (std::getline(log, line)) {
        if (line.find("SUCCESS") != std::string::npos) total_assets++;
    }
    log.close();

    if (total_assets >= MILESTONE) {
        std::cout << "\n\a" << std::endl; // Terminal Bell
        std::cout << "****************************************" << std::endl;
        std::cout << "!!! MILESTONE REACHED: 0,000 + AUDITED !!!" << std::endl;
        std::cout << "NODE 1501 PEARL ST IS NOW A HIGH-VALUE ASSET." << std::endl;
        std::cout << "****************************************" << std::endl;
    }
    return 0;
}
