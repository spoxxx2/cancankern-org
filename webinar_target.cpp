#include <iostream>
#include <string>

void executive_rank(std::string name) {
    std::cout << "Analysis for: " << name << std::endl;
    if (name == "Zoe Heller") {
        std::cout << "[DIRECTOR LEVEL] STRATEGIC TARGET. DO NOT COLD-EMAIL." << std::endl;
        std::cout << "ACTION: PITCH VIA FORMAL WHITE PAPER ONLY." << std::endl;
    } else if (name == "Zac Meyer" || name == "Cara Morgan") {
        std::cout << "[DECISION MAKER] HIGH PRIORITY." << std::endl;
        std::cout << "ACTION: SEND MOU AND PROCUREMENT SPECS." << std::endl;
    } else if (name == "Rhonalyn Cabello") {
        std::cout << "[PR / OUTREACH] VISIBILITY TARGET." << std::endl;
        std::cout << "ACTION: OFFER NODE 1501-P AS A CASE STUDY." << std::endl;
    } else {
        std::cout << "[STAFF LEVEL] PROVIDE TECHNICAL BRIEF." << std::endl;
    }
    std::cout << "---------------------------------" << std::endl;
}

int main() {
    executive_rank("Zoe Heller");
    executive_rank("Zac Meyer");
    executive_rank("Cara Morgan");
    return 0;
}
