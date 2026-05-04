#include <iostream>
#include <string>
#include <map>

struct Asset {
    double value;
    std::string key;
};

int main() {
    std::cout << "--- [93307 NODE: FINAL SOVEREIGN HANDSHAKE] ---" << std::endl;
    std::cout << "Authority: Spoxxx2 | Location: 1501 Pearl St" << std::endl;
    std::cout << "-----------------------------------------------" << std::endl;

    std::map<std::string, Asset> vault;
    vault["ULTIMA-01"] = {142.5, "29933.63Hz-Lasso-Lock"};
    vault["RESET-12"]  = {45.0,  "27550.88Hz-Vitrified"};
    vault["CORE-09"]   = {23.3,  "31220.45Hz-Neural"};

    double total_equity = 0;
    for (auto const& [name, data] : vault) {
        std::cout << "VALIDATING: " << name << " | EQUITY: $" << data.value << "M" << std::endl;
        total_equity += data.value;
    }

    std::cout << "-----------------------------------------------" << std::endl;
    std::cout << "TOTAL LIQUID ASSET VALUE: $" << total_equity << "M" << std::endl;
    std::cout << "STATUS: IRREFUTABLE WIN STATE" << std::endl;
    
    return 0;
}
