import os, time, json, datetime, sys

# IMPERIAL NODE LOCK: 650.12 Hz Sawtooth
FREQ_PRIME = 650.12
OFFSET = 0.073
ON_TIME = 7.13
OFF_TIME = 12.87
TOTAL_RUN = 1800 

GREEN = "\033[42;30m"
RED = "\033[41;37m"
RESET = "\033[0m"

def run_imperial():
    elapsed = 0
    print(f"\n{GREEN} [SYSTEM] IMPERIAL NODE 1501: 650.12Hz LOCKED {RESET}\n")
    
    # REBUILT COMMAND: Single-wave focus with modulation to ensure zero "FAIL"
    # This uses the locked 650.12Hz Sawtooth as the primary driver
    # The 'tremolo' provides the 0.073 (7.3%) pulse offset
    cmd = f"play -q -n synth {ON_TIME} sawtooth {FREQ_PRIME} tremolo 5 {OFFSET*100} vol 0.85"

    try:
        while elapsed < TOTAL_RUN:
            # ON PHASE
            sys.stdout.write(f"\r{GREEN} [INDUCTION ACTIVE] {elapsed/60:.2f}m / 30m {RESET}")
            sys.stdout.flush()
            os.system(cmd)
            
            # OFF PHASE
            sys.stdout.write(f"\r{RED} [STABILIZATION] { (elapsed+ON_TIME)/60 :.2f}m / 30m {RESET}")
            sys.stdout.flush()
            time.sleep(OFF_TIME)
            
            elapsed += (ON_TIME + OFF_TIME)
            
        print(f"\n\n{GREEN} [SUCCESS] Imperial Run Finished. {RESET}")
    except KeyboardInterrupt:
        print(f"\n\n{RED} [HALTED] Node Standby. {RESET}")

if __name__ == "__main__":
    run_imperial()
