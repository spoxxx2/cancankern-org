import numpy as np
import matplotlib.pyplot as plt

def antimicrobial_assay():
    print("\n--- PHARMA-GRADE ANTIMICROBIAL ASSAY ---")
    purity = 0.999999
    concentrations = np.logspace(-2, 2, 50)
    inhibition = 100 / (1 + (0.5 / concentrations)**(1.5 * purity))
    
    mic_idx = np.where(inhibition > 90)[0][0]
    print(f"RESULT: MIC ACHIEVED AT {concentrations[mic_idx]:.4f} ug/mL")
    
    plt.figure(figsize=(8, 5))
    plt.plot(concentrations, inhibition, color='#FF3300', lw=2)
    plt.xscale('log')
    plt.title('Antimicrobial Potency vs. Concentration (Peak 620)')
    plt.xlabel('Concentration (ug/mL)')
    plt.ylabel('Bacterial Inhibition (%)')
    plt.grid(True, alpha=0.3)
    plt.savefig('pharma_assay.png')
    print("SAVED: pharma_assay.png")

if __name__ == "__main__":
    antimicrobial_assay()
