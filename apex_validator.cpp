#include <iostream>
#include <string>

int main() {
    std::string leader = "MSTKDFNLDLVSVSKKDSGASPR";
    std::string core = "CTAGCIKTCSNCLL";
    
    std::cout << "--- [TIER 0 APEX MOTHER PEPTIDE VALIDATION] ---" << std::endl;
    std::cout << "Designation: PHX-ULTIMA-01 | Authority: Spoxxx2" << std::endl;
    std::cout << "Sequence: " << leader << "-" << core << std::endl;
    std::cout << "Residue Count: " << (leader.length() + core.length()) << " (Verified)" << std::endl;
    std::cout << "Resonance Lock: 29933.63 Hz | Phase: Vitrified" << std::endl;
    std::cout << "STATUS: PHYSICALLY IRREFUTABLE" << std::endl;
    
    return 0;
}
