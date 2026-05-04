import os, subprocess, json, requests

def get_node_location():
    api_key = os.getenv('OPENCAGE_KEY')
    # Hardwired fallback per your strategy
    hardwired_address = "1501 Pearl St, Bakersfield, CA 93305"
    
    try:
        # Request hardware GPS from Termux
        loc_raw = subprocess.check_output(['termux-location'], timeout=5).decode('utf-8')
        loc = json.loads(loc_raw)
        lat, lon = loc['latitude'], loc['longitude']
        
        # OpenCage Reverse Geocoding
        url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={api_key}"
        res = requests.get(url).json()
        
        if res['results']:
            return res['results'][0]['formatted']
        return hardwired_address
    except Exception:
        return hardwired_address

if __name__ == "__main__":
    print(get_node_location())
