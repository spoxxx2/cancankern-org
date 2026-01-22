#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <iomanip>

struct DigitalTwin {
    std::string material;
    std::string subtype;
    std::string condition;
    std::string disposal;
    double mass_kg;
    double spectral_id;
};

void execute_overlord_audit(DigitalTwin audit) {
    std::ofstream vault("audit_success.log", std::ios_base::app);
    std::string yrs10, yrs25, yrs50;
    double bsf_yield = 0.0;

    if (audit.material == "Ferrous Metal") {
        yrs10 = "Oxidation Patina (Fe2O3). Structural loss: 5%.";
        yrs25 = "Severe pitting. Danger: Sharp edges/Leachate.";
        yrs50 = "Complete mineralization. Worth: $0.00.";
    } else if (audit.material == "Organic" || audit.material == "Cellulose") {
        yrs10 = "Complete Decomposition.";
        yrs25 = "N/A - Nutrient Cycle Integrated.";
        yrs50 = "N/A - Soil Carbon Sequestration.";
        bsf_yield = audit.mass_kg * 0.20; 
    }

    vault << "{\n"
          << "  \"digital_twin_id\": \"AUD-V-" << time(0) << "\",\n"
          << "  \"taxonomy\": {\n"
          << "    \"material\": \"" << audit.material << "\",\n"
          << "    \"subtype\": \"" << audit.subtype << "\",\n"
          << "    \"condition\": \"" << audit.condition << "\",\n"
          << "    \"disposal\": \"" << audit.disposal << "\"\n"
          << "  },\n"
          << "  \"spectral_calibration\": {\"fingerprint_id\": " << audit.spectral_id << "},\n"
          << "  \"biomass_forecast\": {\"bsf_protein_yield_kg\": " << std::fixed << std::setprecision(2) << bsf_yield << "},\n"
          << "  \"forecast_breakdown\": {\n"
          << "    \"10_year\": \"" << yrs10 << "\",\n"
          << "    \"25_year\": \"" << yrs25 << "\",\n"
          << "    \"50_year\": \"" << yrs50 << "\"\n"
          << "  },\n"
          << "  \"status\": \"VERIFIED_GOLDEN\"\n"
          << "}\n---\n";

    vault.close();
    std::cout << ">>> [GOLDEN OVERLORD] Data Hardwired. BSF Yield: " << bsf_yield << "kg" << std::endl;
}

int main() {
    DigitalTwin scan = {"Organic", "Food Waste", "Wet", "BSF", 5.0, 450.22};
    execute_overlord_audit(scan);
    return 0;
}
