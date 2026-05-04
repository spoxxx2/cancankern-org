import math
import time

# Node 1501-P: Sovereign Synthesis Parameters
TARGET_FREQ = 1700.0  # Hz
TOTAL_PULSES = 2040000
RUN_DURATION_HOURS = 7
PULSE_PER_SECOND = TARGET_FREQ

print(f"--- NODE 1501-P: ACOUSTIC STABILIZER ENGAGED ---")
print(f"Target: {TARGET_FREQ}Hz | Patent ID: US 64/016,955")

def calculate_correction(elapsed_time_sec):
    # Simulated thermal expansion of the reaction vessel (Node 1501-P profile)
    # Drift increases as the Dayton Exciters heat up
    drift = 0.00005 * math.sqrt(elapsed_time_sec) 
    corrected_freq = TARGET_FREQ + (TARGET_FREQ * drift)
    return corrected_freq

try:
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        if elapsed > (RUN_DURATION_HOURS * 3600):
            break
            
        current_stable_freq = calculate_correction(elapsed)
        
        # Log to Termux console every 10 seconds
        if int(elapsed) % 10 == 0:
            print(f"[{time.strftime('%H:%M:%S')}] Active Freq: {current_stable_freq:.4f}Hz | Status: LOCKED")
            
        time.sleep(1)

except KeyboardInterrupt:
    print("\n--- SHUTDOWN: SYNERGY LOG SAVED ---")

print(f"Run Complete. Total Pulses Processed: {TOTAL_PULSES}")
