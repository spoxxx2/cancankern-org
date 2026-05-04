import sqlite3

def update_alpha(generation_id):
    conn = sqlite3.connect('/data/data/com.termux/files/home/overlord_vault.db')
    c = conn.cursor()
    
    # Calculate average efficiency of the previous generation
    c.execute("SELECT AVG(peptide_grams / 3.0) FROM audits WHERE generation_id = ?", (generation_id-1,))
    prev_eff = c.fetchone()[0] or 1.0
    
    c.execute("SELECT AVG(peptide_grams / 3.0) FROM audits WHERE generation_id = ?", (generation_id,))
    curr_eff = c.fetchone()[0] or 1.0
    
    # Genetic Alpha (α) is the improvement coefficient
    alpha = round(curr_eff / prev_eff, 4)
    
    print(f"🔱 GENETIC DRIFT DETECTED: Alpha-Score {alpha}")
    print(f"STRATEGY: {'Accelerate Induction' if alpha > 1.05 else 'Maintain 650Hz Baseline'}")
    
    conn.close()
