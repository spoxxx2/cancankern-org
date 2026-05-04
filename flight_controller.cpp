#include <iostream>
#include <map>

/* * PROJECT: CANCAN FLIGHT CONTROLLER V7.6
 * FEATURE: VOLTAGE-TO-ALTITUDE MAPPING (VAM)
 */

int main() {
    // Map: Battery Voltage (V) -> Target Altitude (ft)
    std::map<double, int> altitude_map;
    altitude_map[12.0] = 500;   // Critical Low: Safe Descent
    altitude_map[13.2] = 2500;  // Nominal: Loitering
    altitude_map[14.4] = 5500;  // Peak Charge: Stratospheric Harvest

    double current_volts = 14.1; 
    int target_alt = 0;

    for (auto const& [volts, alt] : altitude_map) {
        if (current_volts >= volts) target_alt = alt;
    }

    std::cout << "--- VAM SYSTEM: ACTIVE ---" << std::endl;
    std::cout << "Current Bus Voltage: " << current_volts << "V" << std::endl;
    std::cout << "Target Altitude: " << target_alt << " FT" << std::endl;
    std::cout << "Status: OPTIMIZING FOR PEAK SOLAR GAIN" << std::endl;

    return 0;
}
