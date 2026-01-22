#include <iostream>
#include <fstream>
#include <string>
#include <sys/stat.h>
#include <ctime>
#include <sstream>
#include <iomanip>

// --- SETTINGS & STRATEGY ---
std::string get_env_var(std::string key) {
    std::ifstream env(".env");
    std::string line;
    while (std::getline(env, line)) {
        if (line.find(key + "=") == 0) return line.substr(key.length() + 1);
    }
    return "";
}

// --- FORENSIC LOGIC ---
std::string calculate_spectral_fingerprint() {
    return "BSFL-SPEC-" + std::to_string(time(0)).substr(4, 6);
}

std::string get_bakersfield_ward(double lat, double lon) {
    if (lat > 35.4) return "Ward 3 (Ken Weir)";
    if (lon < -119.05) return "Ward 4 (Bob Smith)";
    if (lat < 35.35 && lon > -119.0) return "Ward 2 (Andrae Gonzales)";
    return "Ward 1 (Eric Arias)"; 
}

// --- THE CORE ENGINE ---
int main(int argc, char* argv[]) {
    mkdir("data", 0777); mkdir("vault", 0777);
    std::string mode = (argc > 1) ? argv[1] : "";

    if (mode == "--field") {
        system("termux-volume music 100");
        std::cout << "\033[1;33;40m" << "=== FIELD MODE ACTIVATED ===" << "\033[0m" << std::endl;
        system("termux-tts-speak 'Bakersfield Field Mode Active.'");
    } else if (mode == "--sync") {
        system("git add . && git commit -m 'Strategy Sync' && git push origin main");
    } else {
        // Standard Audit with Ward & Spectral logic
        double lat = 35.3733; // Mock GPS (Will pull from your real GPS logic)
        double lon = -119.0187;
        
        std::string ward = get_bakersfield_ward(lat, lon);
        std::string spec = calculate_spectral_fingerprint();

        std::ofstream log("vault/digital_twin_log.json", std::ios_base::app);
        log << "{\"event\":\"audit\", \"ward\":\"" << ward << "\", \"spec\":\"" << spec << "\"}" << std::endl;
        
        std::cout << "\033[1;32m" << "--- AUDIT SECURED [" << ward << "] ---" << "\033[0m" << std::endl;
        system("termux-tts-speak 'Audit secured in " + ward + "'");
    }
    return 0;
}
