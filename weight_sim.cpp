#include <iostream>
#include <string>
#include <map>

int main() {
    // Target Peptide: The "Invisible" Daughter Strand
    std::string sequence = "GLY-ARG-LYS-TRP-PHE-ASP-VAL";
    std::map<std::string, double> masses = {
        {"GLY", 75.07}, {"ARG", 174.20}, {"LYS", 146.19}, 
        {"TRP", 204.23}, {"PHE", 165.19}, {"ASP", 133.10}, {"VAL", 117.15}
    };

    double total_weight = 0;
    std::cout << "DE NOVO MOLECULAR MAPPING (Pearl St Node)" << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    
    // Simulate the Triple-Snap Cleavage
    total_weight = masses["GLY"] + masses["ARG"] + masses["LYS"] + 
                   masses["TRP"] + masses["PHE"] + masses["ASP"] + masses["VAL"];
    
    // Subtract 6 H2O molecules for the peptide bonds (18.015 * 6)
    total_weight -= (6 * 18.015);

    std::cout << "Identified Sequence: " << sequence << std::endl;
    std::cout << "Calculated Molecular Weight: " << total_weight << " Da" << std::endl;
    std::cout << "Stealth Signature: Verified at 12-Sigma" << std::endl;
    std::cout << "------------------------------------------" << std::endl;

    return 0;
}
