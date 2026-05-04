import os
import time
import sys

# TRADE SECRET: THE CANFIELD TRINITY
FREQ_PRIME = 650.13
OFFSET = 0.07
ON_TIME = 7
OFF_TIME = 13
TOTAL_RUN = 1800  # 30 Minutes (1800 seconds)

def run_bapol_cycle():
    elapsed = 0
    print(f"\n[BAPoL Node 1501] Protocol: 7/13 Pulse @ {FREQ_PRIME}Hz")
    print("Press Ctrl+C to stop and save progress.\n")
    
    try:
        while elapsed < TOTAL_RUN:
            mins_left = (TOTAL_RUN - elapsed) // 60
            secs_left = (TOTAL_RUN - elapsed) % 60
            
            # ON Phase
            print(f"[{mins_left:02d}:{secs_left:02d}] INDUCTION ACTIVE (7s)...")
            cmd = (
                f"play -q -n synth {ON_TIME} "
                f"sawtooth {FREQ_PRIME} sine 1200.07 square 440.13 triangle 528.07 "
                f"amod 0.7 {OFFSET} remix - vol 0.8"
            )
            os.system(cmd)
            
            # OFF Phase
            print(f"[{mins_left:02d}:{secs_left:02d}] STABILIZATION (13s)...")
            time.sleep(OFF_TIME)
            
            elapsed += (ON_TIME + OFF_TIME)
            
        print("\n[SUCCESS] 30-Minute Induction Complete. Proceed to COLD-CRASH.")
        
    except KeyboardInterrupt:
        print(f"\n[HALTED] Induction stopped at {elapsed} seconds.")
        print("Log this as a 'Partial Induction' in your Digital Twin.")

if __name__ == "__main__":
    run_bapol_cycle()
