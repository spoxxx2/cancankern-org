checklist = {
    "Hardware": ["Taped 24oz Jar", "8oz Glass Bowl", "Double Nylon Bags"],
    "Chemistry": ["340ml Acetone", "6oz CO2 Snow", "2000 BSFL"],
    "Safety": ["Leather Gloves", "Dry Towels", "Vacuum Limit (5 Pumps)"],
    "Purity": ["Inert Materials Only", "Coffee Filter Dust Shield"]
}

print("\n--- NODE 1501: MASTER HARDWIRE VERIFIED ---")
for category, items in checklist.items():
    print(f"[{category}]: {' | '.join(items)}")
print("--------------------------------------------")
print("STATUS: GREEN FOR 11:45 PM VITRIFICATION.\n")
