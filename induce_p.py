import os
import time

# THE PLATINUM TRINITY (CANFIELD NODE 1501)
FREQ_PRIME = 650.137
OFFSET = 0.073
ON_TIME = 7.13
OFF_TIME = 12.87
TOTAL_RUN = 1800 

def run_platinum_cycle():
    elapsed = 0
    print(f"\n[PLATINUM MODE] Node 1501 Active. Freq: {FREQ_PRIME}Hz")
    
    try:
        while elapsed < TOTAL_RUN:
            print(f"[{elapsed:.2f}s] INDUCTION (7.13s)...")
            
            # The 12-Wave Fractal Stack
            cmd = (
                f"play -q -n synth {ON_TIME} "
                f"sawtooth {FREQ_PRIME} sine 1200.073 square 440.137 triangle 528.073 "
                f"sine 5000 sine 8000 sine 12000 sine 15000 "
                f"sine 20 sine 40 sine 60 "
                f"amod 0.7 {OFFSET} remix - vol 0.85"
            )
            os.system(cmd)
            
            print(f"[{elapsed + ON_TIME:.2f}s] STABILIZATION (12.87s)...")
            time.sleep(OFF_TIME)
            
            elapsed += (ON_TIME + OFF_TIME)
            
        print("\n[COMPLETE] Platinum Yield Recovery Ready.")
        
    except KeyboardInterrupt:
        print(f"\n[HALTED] Stopped at {elapsed:.2f}s.")

if __name__ == "__main__":
    run_platinum_cycle()
