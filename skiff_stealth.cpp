#include <iostream>

void set_lift_profile(double hz, bool stealth_mode) {
    if (hz == 650.0 && stealth_mode) {
        std::cout << "[*] PHASE CANCELING ACTIVE: SILENT LIFT ENABLED" << std::endl;
        std::cout << "[*] OUTPUT: 0.0 dB AT 50 FEET" << std::endl;
    } else {
        std::cout << "[!] WARNING: ACOUSTIC SIGNATURE DETECTABLE" << std::endl;
    }
}

int main() {
    set_lift_profile(650.0, true);
    return 0;
}
