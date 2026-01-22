#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::string auditID = "BFL-2026-005";
    std::string material = "Cellulose/Paper";
    int accuracy = 99;

    std::ofstream file;
    file.open("audits.json", std::ios::app); 
    file << "{\"id\": \"" << auditID << "\", \"type\": \"" << material << "\", \"score\": " << accuracy << "}" << std::endl;
    file.close();

    std::cout << "Audit " << auditID << " hardwired to the ledger." << std::endl;
    return 0;
}
