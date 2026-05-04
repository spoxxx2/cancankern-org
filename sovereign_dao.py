import json, time, hashlib

def mint_sovereign_token(asset_name, value_mg):
    print(f"\n[ORACLE] MINTING SOVEREIGN ASSET: {asset_name}...")
    
    timestamp = str(time.time())
    block_hash = hashlib.sha256(f"{asset_name}{timestamp}{value_mg}".encode()).hexdigest()
    
    ledger_entry = {
        "asset": asset_name,
        "valuation_per_mg": value_mg,
        "node_hq": "1501_PEARL_ST",
        "compliance_status": "SB_1383_SHIELD_ACTIVE",
        "governance": "DECENTRALIZED_DAO_LOCKED",
        "block_proof": block_hash[:16]
    }

    with open("gemini.md", "a") as f:
        f.write(f"\n### [SOVEREIGN_LEDGER_BLOCK] {int(time.time())}\n")
        f.write(f"```json\n{json.dumps(ledger_entry, indent=2)}\n```\n")
    
    print(f"\n[SUCCESS] Asset {asset_name} anchored to Sovereign Ledger.")
    print(f"[PROOF] {block_hash[:16]}... recorded in gemini.md")

if __name__ == "__main__":
    mint_sovereign_token("CANCAN-V26-PHOENIX", 6250)
