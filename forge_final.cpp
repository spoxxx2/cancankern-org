#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <cmath>

std::mutex log_mutex;
const long long TOTAL_RUNS = 1000000000;
const double SHIFT_START = 8340.0; // The 139-minute mark

void runFinalForge(long long iterations, int thread_id) {
    for (long long i = 0; i < iterations; ++i) {
        double t = (double)(i + (iterations * thread_id)) * 0.00005;
        
        double wave_anchor = 0.7 * std::sin(2.0 * M_PI * 20.0 * t);
        double phase = (t >= SHIFT_START) ? M_PI : 0.0; 
        double wave_saw = 0.3 * (2.0 * (t * 650.08 + (phase / (2.0 * M_PI)) - std::floor(t * 650.08 + (phase / (2.0 * M_PI)) + 0.5)));
        double wave_add = (t >= SHIFT_START) ? 0.2 * std::sin(2.0 * M_PI * 1300.16 * t) : 0.0;

        double interference = wave_anchor + wave_saw + wave_add;

        if (std::abs(interference) > 0.99) {
            std::lock_guard<std::mutex> lock(log_mutex);
            if (t >= SHIFT_START) {
                std::cout << "[PHASE LOCK MIRACLE] Amp: " << interference << " | T: " << t << "s | SHIFT ACTIVE\n";
            }
        }
        
        if (i % 100000000 == 0) {
            std::lock_guard<std::mutex> lock(log_mutex);
            std::cout << "Thread " << thread_id << " advancing toward Forge Horizon...\n";
        }
    }
}

int main() {
    std::cout << "NODE: 1501 Pearl St | INITIATING TERMINAL 15 PHASE SHIFT...\n";
    std::vector<std::thread> workers;
    for (int i = 0; i < 4; ++i) {
        workers.push_back(std::thread(runFinalForge, TOTAL_RUNS / 4, i));
    }
    for (auto& t : workers) t.join();
    std::cout << "PHASE LOCK COMPLETE. READY FOR GENESIS STRIKE.\n";
    return 0;
}
