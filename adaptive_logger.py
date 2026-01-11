import os, sys, random
from datetime import datetime

sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))
from supabase import create_client

SUPABASE_URL = "https://dzrnwzvizztfmjgvpajd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I"

def log_debris_event(metadata):
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # High-Value "Buyer" Metadata Integration
        metadata["market_data"] = {
            "purity_score": round(random.uniform(85.0, 99.9), 1), # % of polymer purity
            "moisture_content": f"{random.randint(2, 15)}%",      # High moisture = lower price
            "weight_est_grams": random.randint(20, 500),         # Weight = Volume for logistics
            "current_market_price_mt": random.randint(800, 1200) # Price per metric ton
        }
        
        metadata["forecast_50yr"] = {
            "appearance": "Micro-plastic fragmentation",
            "danger_level": "High - Leachate Risk",
            "worth_at_50yrs": "$0.00 (Degraded)"
        }
        
        response = supabase.table("debris_logs").insert(metadata).execute()
        print(f"✅ HIGH-VALUE DATA LOGGED: {metadata['event_id']}")
        return response
    except Exception as e:
        print(f"❌ Sync Failed: {e}")

if __name__ == "__main__":
    test_data = {
        "event_id": f"SALE-DATA-{random.randint(1000,9999)}",
        "objects": {
            "material": "Polymer",
            "sub_type": "PET #1",
            "condition": "Intact",
            "disposal": "Circular Economy"
        }
    }
    log_debris_event(test_data)
