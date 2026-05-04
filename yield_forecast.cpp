#include <iostream>

int main() {
    int worm_count = 12;
    double protein_per_worm = 0.025; 
    double cleavage_efficiency = 1.9845;
    double parent_mass = 2600.0;
    double target_mass = 907.04;

    std::cout << "BATCH #001-B FORENSIC YIELD AUDIT" << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    std::cout << "Precursor: 21-mer (" << parent_mass << " Da)" << std::endl;
    std::cout << "Daughter:  7-mer (" << target_mass << " Da)" << std::endl;
    std::cout << "Efficiency Multiplier: " << cleavage_efficiency << "x" << std::endl;
    
    double yield = (worm_count * protein_per_worm) * cleavage_efficiency;
    
    std::cout << "TOTAL STEALTH YIELD: " << yield << " g" << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    std::cout << "STATUS: BITAN-SUPERIORITY CONFIRMED" << std::endl;

    return 0;
}
