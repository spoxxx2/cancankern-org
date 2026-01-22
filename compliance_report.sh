#!/bin/bash
# CANCAN SB 1383 Annual Reporting Tool
# Administrator: Casey Canfield

YEAR=$(date +%Y)
TOTAL_LBS=$(grep "recovered_weight" audit_logs/*.json | awk -F: '{sum+=$2} END {print sum}')

echo "--- OFFICIAL SB 1383 COMPLIANCE REPORT ---"
echo "Reporting Year: $YEAR"
echo "Organization: CANCAN (EIN: 39-2261270)"
echo "Address: 1501 Pearl St, 93305"
echo "------------------------------------------"
echo "TOTAL EDIBLE FOOD RECOVERED: $TOTAL_LBS lbs"
echo "TOTAL ORGANIC WASTE DIVERTED: [Calculated via DOI Engine]"
echo "------------------------------------------"
echo "This report is generated using the DOI: 10.5281/zenodo.18286490 methodology."
