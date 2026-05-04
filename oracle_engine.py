import numpy as np
from scipy.stats import linregress
import sqlite3

def calculate_oracle_signal():
    conn = sqlite3.connect('overlord_vault.db')
    # Pull metabolic efficiency and AQI to verify "Environmental Stress"
    data = conn.execute("SELECT peptide_grams, thermal_c, aqi FROM audits ORDER BY timestamp DESC LIMIT 20").fetchall()
    
    if len(data) < 2: return "WAITING FOR DATA..."

    efficiency = [row[0] for row in data]
    x = np.arange(len(efficiency))
    
    # Linear Regression to find the "Metabolic Velocity"
    slope, intercept, r_value, p_value, std_err = linregress(x, efficiency)
    
    # SIGNAL GENERATION
    if slope > 0.05:
        signal = "💹 BULLISH: Waste Stream Enrichment (Local Supply Stabilizing)"
    elif slope < -0.05:
        signal = "⚠️ BEARISH: Nutritional Decay (Supply Chain Volatility Detected)"
    else:
        signal = "⚖️ NEUTRAL: Metabolic Equilibrium"
        
    print(f"🔱 ORACLE SIGNAL: {signal}")
    print(f"🔱 CONFIDENCE (R²): {r_value**2:.4f}")
    conn.close()

if __name__ == "__main__":
    calculate_oracle_signal()
