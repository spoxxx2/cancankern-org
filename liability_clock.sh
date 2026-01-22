#!/bin/bash
# CANCAN - Liability Projection Engine
# Administrator: Casey Canfield | UEI: SSWWJ3SEMZ73

# Hardcoded constants based on 50-year decay models
COST_PER_TON_LEACHATE=450 # Estimated cleanup cost
DEGRADATION_RATE=0.02     # Annual compounding risk

echo "--- CANCAN LIABILITY PROJECTION ---"
echo "LOCATION: 1501 PEARL ST, 93305"
echo "METHODOLOGY: DOI 10.5281/zenodo.18286490"
echo "-----------------------------------"

read -p "Estimated Tons of Unmanaged Organic Waste: " TONS

CURRENT_LIABILITY=$(echo "$TONS * $COST_PER_TON_LEACHATE" | bc)
YEAR_50_LIABILITY=$(echo "$CURRENT_LIABILITY * (1 + $DEGRADATION_RATE)^50" | bc)

echo ""
echo "IMMEDIATE REMEDIATION VALUE: $$CURRENT_LIABILITY"
echo "50-YEAR PROJECTED UNMANAGED LIABILITY: $$YEAR_50_LIABILITY"
echo ""
echo "CANCAN BSFL DIVERSION SAVINGS: 98.4%"
echo "-----------------------------------"
