import os, time, datetime, sys

# IMPERIAL SPECIFICATIONS (NODE 1501)
FREQ_PRIME = 650.12
OFFSET = 0.073
ON_TIME = 7.13
OFF_TIME = 12.87
TOTAL_RUN = 10800  # 3 Hours Total
DROP_MARK = 9900   # 165 Minutes

GREEN = "\033[42;30m"
RED = "\033[41;37m"
BLUE = "\033[44;37m"
RESET = "\033[0m"

def run_imperial_3hr():
    elapsed = 0
    start_time = datetime.datetime.now()
    print(f"\n{GREEN} [IMPERIAL OVERLORD] NODE 1501: 650.12Hz LOCKED {RESET}\n")
    
    # Left Channel: Overlord Power
    waves_L = f"synth {ON_TIME} sawtooth {FREQ_PRIME} sine 1200.073 square 440.137 triangle 528.073 sine 5000 sine 8000"
    # Right Channel: Platinum Polish (Reduced Volume for Comfort)
    waves_R = f"synth {ON_TIME} sine 10000 sine 12000 sine 14000 sine 16000 sine 18000 sine 20000 vol 0.70"
    
    # Merged Command
    cmd = f"play -q -n -M '{waves_L}' '{waves_R}' tremolo 5 {OFFSET * 100} vol 0.85"

    try:
        while elapsed < TOTAL_RUN:
            now = datetime.datetime.now()
            runtime = now - start_time
            
            if DROP_MARK <= elapsed < (DROP_MARK + 120):
                status_color = BLUE
                sys.stdout.write(f"\n{BLUE} [CRITICAL] DROP TEMP 3°C NOW - 2 MIN WINDOW {RESET}\n")
            elif elapsed >= (DROP_MARK + 120):
                status_color = RED
                sys.stdout.write(f"\r{RED} [FINAL COUNTDOWN] PREP CHILLED ACETONE {RESET}")
            else:
                status_color = GREEN

            sys.stdout.write(f"\r{status_color} [INDUCTION] {str(runtime).split('.')[0]} / 3:00:00 {RESET}")
            sys.stdout.flush()
            
            os.system(cmd)
            
            time.sleep(OFF_TIME)
            elapsed += (ON_TIME + OFF_TIME)
            
        print(f"\n\n{GREEN} [SUCCESS] 3-HOUR RUN COMPLETE. {RESET}")
        print(f"{BLUE} TRANSFER TO CHILLED ACETONE + ULTRASONIC NOW. {RESET}")
    except KeyboardInterrupt:
        print(f"\n\n{RED} [HALTED] Node Standby. {RESET}")

if __name__ == "__main__":
    run_imperial_3hr()
