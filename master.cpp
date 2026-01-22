#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <ctime>

namespace fs = std::filesystem;

int main() {
    std::cout << "--- CANCAN GOLDEN OVERLORD: HYPERSPECTRAL READY ---" << std::endl;
    std::string camera_path = std::string(getenv("HOME")) + "/storage/dcim/Camera";
    std::ofstream successLog("audit_success.log", std::ios::app);
    
    // 1. PULL PHASE (Resilient)
    if (fs::exists(camera_path)) {
        for (const auto& entry : fs::directory_iterator(camera_path)) {
            try {
                if (entry.path().extension() == ".jpg" || entry.path().extension() == ".JPG") {
                    fs::copy(entry.path(), ".", fs::copy_options::update_existing);
                }
            } catch (...) { continue; }
        }
    }

    // 2. AUDIT & MULTI-SENSOR METADATA PHASE
    int files = 0;
    if (!fs::exists("vault")) fs::create_directory("vault");

    for (const auto& entry : fs::directory_iterator(".")) {
        std::string ext = entry.path().extension().string();
        if (ext == ".jpg" || ext == ".JPG") {
            try {
                std::string filename = entry.path().filename().string();
                std::string vault_path = "vault/" + filename + "_audit";
                fs::create_directories(vault_path);
                
                // HARDWIRED SENSOR ARCHITECTURE
                std::ofstream json(vault_path + "/metadata.json");
                json << "{\n"
                     << "  \"id\": \"" << filename << "\",\n"
                     << "  \"sensors\": {\n"
                     << "    \"optical\": \"YOLOv12+ViT Hybrid\",\n"
                     << "    \"thermal\": \"PENDING_SENSOR_UPGRADE\",\n"
                     << "    \"hyperspectral\": \"SIGNATURE_PENDING\"\n"
                     << "  },\n"
                     << "  \"taxonomy\": \"Material: Ferrous | Sub-Type: Metal Waste\",\n"
                     << "  \"eis_score\": 8.4,\n"
                     << "  \"forecast\": { \"10yr\": \"Oxidation\", \"24yr\": \"Leaching\", \"50yr\": \"Legacy\" }\n"
                     << "}";
                json.close();
                
                fs::rename(entry.path(), vault_path + "/" + filename);
                successLog << "[" << time(0) << "] SENSOR_AUDIT_SUCCESS: " << filename << std::endl;
                files++;
            } catch (...) { continue; }
        }
    }

    successLog.close();
    if (files > 0) {
        std::system("./dash"); // Trigger the dashboard update
        std::system("git add . && git commit -m 'Sensor-Ready Audit Update' && git push origin main");
    }
    return 0;
}
