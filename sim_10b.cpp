#include <iostream>
#include <omp.h>

int main() {
    long long total_runs = 10000000000LL; 
    double total_value = 0;
    
    std::cout << "Starting 10 Billion Runs on Panama Lane Node..." << std::endl;
    double start = omp_get_wtime();

    #pragma omp parallel for reduction(+:total_value)
    for (long long i = 0; i < total_runs; ++i) {
        total_value += 0.650; // Hardwired 650Hz resonance factor
    }

    double end = omp_get_wtime();
    std::cout << "Simulation Complete in " << (end - start) << " seconds." << std::endl;
    return 0;
}
