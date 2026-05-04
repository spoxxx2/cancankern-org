#include <cstdio>

int main() {
    const char* status = "DIVINE_OVERLORD";
    double yield = 1500.25;
    int nodes = 10000;
    int founding = 1999;

    printf("\n\033[1;33m--- CANCAN SOVEREIGN REPORT ---\033[0m\n");
    printf("Status:    %-15s\n", status);
    printf("Legacy:    Est. %d\n", founding);
    printf("Mesh:      %d Active Nodes\n", nodes);
    printf("Yield:     \033[1;32m$%.2f CANCAN\033[0m\n", yield);
    printf("\033[1;33m-------------------------------\033[0m\n\n");
    return 0;
}
