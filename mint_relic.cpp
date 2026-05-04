#include <iostream>
#include <ctime>

int main() {
    std::time_t now = std::time(0);
    char* dt = std::ctime(&now);

    std::cout << "--- [MINTING] RELIC-CLASS DIGITAL TWIN ---" << std::endl;
    std::cout << "TIMESTAMP: " << dt;
    std::cout << "DOI: 10.5281/zenodo.19590407 [ROOT]" << std::endl;
    std::cout << "KINETIC CALIBRATION: 1588 m/s" << std::endl;
    std::cout << "SIGMA: 27.0 (INDESTRUCTIBLE)" << std::endl;
    
    std::cout << "[STATUS] 1.0 FRACTIONAL UNIT ISSUED TO CANCAN ARCHIVES." << std::endl;
    return 0;
}
