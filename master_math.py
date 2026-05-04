import numpy as np
from scipy.optimize import curve_range
import sqlite3

def log_regression(x, a, b):
    return a + b * np.log(x)

def master_forecast():
    conn = sqlite3.connect('overlord_vault.db')
    # Pull the last 10 audits to verify the trend
    data = conn.execute("SELECT peptide_grams FROM audits ORDER BY timestamp DESC LIMIT 10").fetchall()
    y = np.array([row[0] for row in data])[::-1]
    x = np.arange(1, len(y) + 1)
    
    # Fit the 'Mastery Curve'
    popt, _ = curve_fit(log_regression, x, y)
    next_yield = log_regression(11, *popt)
    
    print(f"🔱 MASTERY FORECAST: Next Batch Yield Estimated at {next_yield:.2f}g")
    print(f"🔱 SYSTEM EFFICIENCY: {popt[1]*100:.1f}% Improvement Rate")

if __name__ == "__main__":
    master_forecast()
