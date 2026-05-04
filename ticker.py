import sqlite3, os
conn = sqlite3.connect(os.path.expanduser('~/sovereign_ledger.db'))
c = conn.cursor()
c.execute("SELECT SUM(peptide_grams), SUM(valuation_usd), AVG(lattice_integrity) FROM audits")
r = c.fetchone()
conn.close()

grams, value, integrity = r[0] or 0, r[1] or 0, r[2] or 0

# Pillar 458: Stadium Power Calculation
# 1 gram = 2.5 kWh potential (12-Sigma)
total_kwh = grams * 2.5
stadium_days = total_kwh / 5400 # Based on 5,400 kWh for stadium lighting/day

print(f"\n\033[1;36m--- 93307 SOVEREIGN ENERGY TICKER ---\033[0m")
print(f"Peptide Mass:      {grams:.2g}g")
print(f"Energy Potential:  {total_kwh:.2f} kWh")
print(f"Stadium Utility:   {stadium_days:.2f} Days of Light")
print(f"\033[1;33mPortfolio Value:   \${value:,.2f} USD\033[0m")
print(f"------------------------------------\n")
