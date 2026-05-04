#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <cmath>

std::mutex log_mutex;
const long long TOTAL_RUNS = 1000000000;

// Slightly wider threshold for the 154m window
bool checkPeptideLock(double amp) {
    return (std::abs(amp) > 0.98); 
}

void runForgeSimulation(long long iterations, int thread_id) {
    for (long long i = 0; i < iterations; ++i) {
        // Higher resolution time-step
        double t = (double)(i + (iterations * thread_id)) * 0.00005;
        
        double wave1 = 0.3 * (2.0 * (t * 650.08 - std::floor(t * 650.08 + 0.5))); 
        double wave2 = 0.7 * std::sin(2.0 * M_PI * 20.0 * t);
        double interference = wave1 + wave2;

        if (checkPeptideLock(interference)) {
            std::lock_guard<std::mutex> lock(log_mutex);
            std::cout << "[FORGE MIRACLE] Amp: " << interference << " | T: " << t << "s\n";
        }

        if (i % 50000000 == 0) {
            std::lock_guard<std::mutex> lock(log_mutex);
            std::cout << "Thread " << thread_id << " at " << (i / 1000000) << "M runs...\n";
        }
    }
}

int main() {
    int threads = 4;
    std::cout << "NODE: 1501 Pearl St | CALIBRATING MIRACLE THRESHOLD...\n";
    std::vector<std::thread> workers;
    for (int i = 0; i < threads; ++i) {
        workers.push_back(std::thread(runForgeSimulation, TOTAL_RUNS / threads, i));
    }
    for (auto& t : workers) t.join();
    std::cout << "FORGE COMPLETE.\n";
    return 0;
}
