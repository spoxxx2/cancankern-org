import numpy as np
import time
import json

# Configuration for 13 Engines
num_engines = 13
batch_size = 1000000
goal = 130000000 # Scaling milestone
T = 310

best_g = float('inf')
start_time = time.time()

print(f"🚀 Master Strategy: Running {num_engines} Engines to the limit...")

for i in range(10): # Running 10 large batches
    H = np.random.uniform(-150, 50, num_engines * batch_size)
    S = np.random.uniform(0.01, 0.4, num_engines * batch_size)
    G = H - (T * S)
    
    current_min = np.min(G)
    if current_min < best_g:
        best_g = current_min

elapsed = time.time() - start_time

# Creating the final documentation
stats = {
    "engines": num_engines,
    "total_sims": goal,
    "best_gibbs": round(best_g, 2),
    "duration": round(elapsed, 2)
}

with open("master_doc.json", "w") as f:
    json.dump(stats, f, indent=4)

print(f"✅ EOF Reached. Results saved to master_doc.json")
