import os, sys
sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))
from supabase import create_client

SUPABASE_URL = "https://dzrnwzvizztfmjgvpajd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I"

def check_scale():
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        response = supabase.table("debris_logs").select("estimated_value", count="exact").execute()
        
        count = response.count
        total_value = sum([item['estimated_value'] for item in response.data if item['estimated_value']])
        
        print(f"\n--- CANCANKERN SCALE MONITOR ---")
        print(f"Current Objects: {count} / 100")
        print(f"Digital Mine Worth: ${total_value:.2f} USD")
        
        if count >= 100:
            print("\n🚨 STRATEGIC MILESTONE REACHED: 100 OBJECTS 🚨")
            print("Action: Export Prospectus and initiate Data Sales contact.")
        else:
            print(f"Progress: { (count/100)*100:.1f}% to Industrial Scale.")
            
    except Exception as e:
        print(f"❌ Monitor Error: {e}")

if __name__ == "__main__":
    check_scale()
