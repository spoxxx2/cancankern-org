#include <iostream>
#include <iomanip>

/* * PROJECT: CANCAN DC-HYBRID (V7.9)
 * MODULE: SALINITY & POWER MONITOR
 */

void check_salinity(double ppm) {
    if (ppm > 35000) { // Sea water threshold
        std::cout << "[!] ALERT: HIGH SALINITY (" << ppm << " PPM)" << std::endl;
        std::cout << "    STATUS: CORROSION RISK ACTIVE - RINSE SENSORS" << std::endl;
    } else {
        std::cout << "[*] SALINITY: " << ppm << " PPM (SOVEREIGN RANGE)" << std::endl;
    }
}

void manage_power(double soc) {
    if (soc < 20.0) {
        std::cout << "[!] ALERT: POWER LOW - EXTRACTION PAUSED" << std::endl;
    } else {
        std::cout << "[*] POWER: " << soc << "% (STABLE)" << std::endl;
    }
}

int main() {
    double current_soc = 88.2;
    double current_salinity = 900.5; // Simulated fresh/brackish mix

    std::cout << "--- NODE 1501-P: SYSTEM CHECK ---" << std::endl;
    manage_power(current_soc);
    check_salinity(current_salinity);
    std::cout << "---------------------------------" << std::endl;
    
    return 0;
}

void check_induction_efficiency(double ppm) {
    if (ppm < 100) {
        std::cout << "[!] NOTICE: SALINITY TOO LOW FOR OPTIMAL PHONON-LOCK" << std::endl;
        std::cout << "    ACTION: ADD 0.5g NaCl TO RECOVER CONDUCTIVITY" << std::endl;
    }
}
