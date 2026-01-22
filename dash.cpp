#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

int main() {
    std::ifstream log("audit_success.log");
    int total_assets = 0;
    while (std::string line; std::getline(log, line)) {
        if (line.find("SUCCESS") != std::string::npos) total_assets++;
    }
    log.close();

    double total_value = total_assets * 840.0;
    
    // Create a lean dashboard string
    std::string new_dash = "<div id=\"stats-dashboard\">";
    new_dash += "<h3>[ NODE_STATS ]</h3>";
    new_dash += "<p>ASSETS: " + std::to_string(total_assets) + "</p>";
    new_dash += "<p>VALUE: $" + std::to_string((int)total_value) + ".00</p></div>";

    // Rewrite a fresh index.html with the new data to avoid appending bloat
    std::system("sed -i 's|<div id=\"stats-dashboard\">.*</div>|" + new_dash + "|' index.html");
    
    return 0;
}
