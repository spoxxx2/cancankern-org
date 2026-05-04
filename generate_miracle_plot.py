import matplotlib
matplotlib.use('Agg') # Force non-interactive mode for Termux
import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(160, 170, 1000)
entropy = np.where(time < 165.57, 8.0 + np.random.normal(0, 0.1, 1000), 0.2)

plt.figure(figsize=(10, 5))
plt.plot(time, entropy, color='green', label='System Entropy')
plt.axvline(x=165.57, color='red', linestyle='--', label='Miracle Mark (165:34)')
plt.title("Excalibur V6.5 Entropy Collapse")
plt.savefig("miracle_plot.png")
print("SUCCESS: miracle_plot.png has been generated in Node 93307.")
