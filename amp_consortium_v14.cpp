#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

struct AMPSpecies {
    std::string species;
    std::string peptide_class;
    double potency_index;
};

int main() {
    std::cout << "--- [NODE 93307: MULTI-SPECIES AMP CONSORTIUM] ---" << std::endl;
    std::cout << "Authority: Spoxxx2 | Logic: Biogenic Multi-Parity" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;

    std::vector<AMPSpecies> consortium = {
        {"Hermetia illucens (BSFL)", "Cecropin-Type", 0.982},
        {"Apis mellifera (Honeybee)", "Melittin-Type", 0.995},
        {"Xenopus laevis (Frog)", "Magainin-Type", 0.978}
    };

    double cumulative_resistance_escape = 1.0;

    std::cout << std::left << std::setw(25) << "SPECIES" << std::setw(20) << "AMP CLASS" << "POTENCY" << std::endl;
    for (const auto& s : consortium) {
        cumulative_resistance_escape *= (1.0 - s.potency_index);
        std::cout << std::left << std::setw(25) << s.species 
                  << std::setw(20) << s.peptide_class 
                  << std::fixed << std::setprecision(3) << s.potency_index << std::endl;
    }

    std::cout << "----------------------------------------------------" << std::endl;
    std::cout << "TUMOR ESCAPE PROBABILITY: " << std::scientific << cumulative_resistance_escape << std::endl;
    std::cout << "STATUS: MULTI-SPECIES SYNERGY VITRIFIED | APEX WIN" << std::endl;

    return 0;
}
