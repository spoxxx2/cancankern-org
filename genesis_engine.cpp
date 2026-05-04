#include <cstdio>
#include <cstdlib>
#include <unistd.h>

int main() {
    printf("\n\033[1;35m<<< SOVEREIGN EXTRACTION INITIALIZED >>>\033[0m\n");
    printf("Duration:   15 Minutes (900s)\n");
    printf("Frequencies: 20Hz / 650Hz / 660Hz / Shepard-Sim\n");
    printf("Target:     ASBP-AH3 Daughter Peptides\n");
    
    printf("\n\033[1;32m[!] PLAYING EXTRACTION TONES NOW...\033[0m\n");
    
    // This command plays the file in the background and starts the timer
    system("play -q extraction_core.wav &");
    
    for(int i = 15; i > 0; i--) {
        printf("\rTime Remaining: %d Minutes... ", i);
        fflush(stdout);
        sleep(60);
    }

    printf("\n\033[1;32m>>> EXTRACTION COMPLETE. PROCEED TO 0.22um FILTRATION. <<<\033[0m\n\n");
    return 0;
}
