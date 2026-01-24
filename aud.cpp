#include <iostream>
#include <string>
#include <sqlite3.h>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    std::string json_payload = argv[1];

    // 1. Local Vault Save
    sqlite3* db;
    sqlite3_open("cancan_audit.db", &db);
    std::string sql = "INSERT INTO debris_logs (full_metadata) VALUES ('" + json_payload + "');";
    sqlite3_exec(db, sql.c_str(), NULL, NULL, NULL);
    sqlite3_close(db);
    std::cout << "🟢 Saved to local vault (1501 Pearl St)." << std::endl;

    // 2. Cloud Sync via Helper Script
    std::string cmd = "./sync_cloud.sh '" + json_payload + "'";
    int res = std::system(cmd.c_str());
    
    if(res == 0) std::cout << "🔵 Cloud Sync Successful." << std::endl;
    else std::cout << "🔴 Cloud Sync Failed (Exit Code: " << res << ")" << std::endl;

    return 0;
}
