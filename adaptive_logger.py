import os, sys, random
from datetime import datetime

sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))
from supabase import create_client

SUPABASE_URL = "https://dzrnwzvizztfmjgvpajd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I"

def log_debris_event(metadata):
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Advanced Multi-Tiered Forecasts
        metadata["forecasts"] = {
            "year_10": "Surface oxidation / Loss of structural polymer elasticity",
            "year_25": "Brittle fragmentation / Soil-interface leaching",
            "year_50": "Micro-plastic saturation / Integral matrix contamination"
        }
        
        metadata["market_data"] = {
            "purity_score": round(random.uniform(85.0, 99.9), 1),
            "current_market_price_mt": random.randint(800, 1200)
        }
        
        response = supabase.table("debris_logs").insert(metadata).execute()
        print(f"✅ MULTI-TIER DATA LOGGED: {metadata['event_id']}")
        return response
    except Exception as e:
        print(f"⚠️ Sync Limited: Check if 'forecasts' column (JSONB) is added to Supabase.")

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
