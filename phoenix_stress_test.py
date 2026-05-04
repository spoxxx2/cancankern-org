import time

def run_phx_sim(batch=100000000, freq=650, mod=20):
    print(f"[PHOENIX] Starting 100M Validation Run...")
    successes = 0
    start = time.time()
    
    # Pre-calculated periods for the 650Hz/20Hz sync
    period_650 = 1.0 / freq
    period_20 = 1.0 / mod
    
    # We report every 1 million runs
    report = 1000000
    
    for i in range(batch):
        # Time-step mapping (simulating the 3-hour extraction window)
        t = (i / batch) * 10800  # 10800 seconds = 3 hours
        
        # SAWTOOTH: (t % period) / period (normalized 0 to 1)
        saw = (t % period_650) / period_650
        
        # SINE: Shifted to 0.0 to 1.0 range
        import math
        sine = (math.sin(2 * math.pi * mod * t) + 1) / 2
        
        # CONSTRUCTIVE INTERFERENCE: 
        # When both waves are in the top 25% of their cycle
        if saw > 0.75 and sine > 0.75:
            successes += 1
            
        if i % report == 0 and i > 0:
            rate = (successes / i) * 100
            print(f"[AUD] Run: {i} | Success: {successes} | Sync Rate: {rate:.4f}% | Node: 93307")

    print(f"[COMPLETE] Final Dataset: {successes} Chameleonic Hits Found.")

run_phx_sim()
