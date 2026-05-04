def run_storage_audit():
    total_mw = 542885.22
    
    # Storage Efficiency Tiers
    peptide_storage = total_mw * 0.15  # 15% locked in molecular folds
    capacitor_capture = total_mw * 0.70 # 70% caught by super-capacitors
    heat_loss = total_mw * 0.15        # 15% thermal bleed
    
    print(f"\n--- STORAGE EFFICIENCY AUDIT ---")
    print(f"Molecular Lock: {peptide_storage:,.2f} MW")
    print(f"Capacitor Bank: {capacitor_capture:,.2f} MW")
    print(f"Sovereign Reserve: {peptide_storage + capacitor_capture:,.2f} MW")
    print(f"> STATUS: 85% RETENTION ACHIEVED.\n")

if __name__ == "__main__":
    run_storage_audit()
