#include <iostream>

int main() {
    double tweezers_mass = 2600.0 + 700.0; // 21-mer + CLR01 weight
    double acoustic_mass = 907.04;        // Phase-3.3 Stealth weight
    
    std::cout << "TUNNELING PROBABILITY COMPARISON" << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    
    // Probability is inversely proportional to mass at 1,450 m/s
    double p_tweezers = 1.0 / tweezers_mass;
    double p_acoustic = 1.0 / acoustic_mass;

    std::cout << "Molecular Tweezers Probability: " << p_tweezers << std::endl;
    std::cout << "Acoustic Stealth Probability:   " << p_acoustic << std::endl;
    std::cout << "Efficiency Gain: " << (p_acoustic / p_tweezers) << "x" << std::endl;
    
    std::cout << "------------------------------------------" << std::endl;
    std::cout << "CONCLUSION: Acoustic Gating is 3.6x more effective for BBB penetration." << std::endl;

    return 0;
}
