import random
import datetime

def get_forecast():
    # Simulated 10B Run Result for 93307 Basin
    predicted_tonnage = round(random.uniform(0.5, 2.3), 2)
    predicted_credits = round(predicted_tonnage * 0.018, 4)
    arrival_time = (datetime.datetime.now() + datetime.timedelta(hours=24)).strftime("%Y-%m-%d %H:00")
    
    print("\n--- 93307 ORACLE FORECAST (PILLAR 375) ---")
    print(f"Next Major Inbound: {arrival_time}")
    print(f"Predicted Tonnage:   {predicted_tonnage} Tons (Produce)")
    print(f"Potential Credits:   {predicted_credits} Methane-Mints")
    print("------------------------------------------\n")

if __name__ == "__main__":
    get_forecast()
