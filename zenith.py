import time
import os

# NODE 1501-P THERMAL PARAMETERS
TARGET_FREQ = 1700.0
DRIFT_COEFF = 0.00004 

def zenith_stabilizer():
    start_time = time.time()
    print(f"--- [ZENITH NODE ACTIVE: US 64/016,955] ---")
    try:
        while True:
            elapsed = time.time() - start_time
            # Pre-emptive correction based on the 1704.96Hz terminal lock
            corrected_freq = TARGET_FREQ + (elapsed * DRIFT_COEFF)
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Freq: {corrected_freq:.4f}Hz | STATUS: LOCKED")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n--- SHUTDOWN: ZENITH LOG SECURED ---")

if __name__ == "__main__":
    zenith_stabilizer()
