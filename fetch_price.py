import requests
import json
import os
from datetime import datetime
from urllib.parse import quote

# List of cases to track: (Market Hash Name, Display Name)
CASES = {
    "Fracture Case": "Fracture Case",
    "Recoil Case": "Recoil Case",
    "Dreams & Nightmares Case": "Dreams & Nightmares Case",
    "Snakebite Case": "Snakebite Case",
    "Operation Broken Fang Case": "Broken Fang Case",
    "Prisma 2 Case": "Prisma 2 Case",
    "Clutch Case": "Clutch Case"
}

URL_TEMPLATE = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}"
DATA_FILE = "/home/q/.openclaw/workspace/website/prices.json"
STATUS_FILE = "/home/q/.openclaw/workspace/website/status.json"

def fetch_price(hash_name):
    try:
        # URL encode the hash name to handle special characters like '&'
        encoded_name = quote(hash_name)
        response = requests.get(URL_TEMPLATE.format(encoded_name), timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("success"):
            # Lowest Price
            low_str = data.get("lowest_price", "0")
            low_price = float(low_str.replace('$', '').replace(',', '').strip())
            
            # Median Price (Used as a proxy for "Higher" asking prices)
            med_str = data.get("median_price", "0")
            med_price = float(med_str.replace('$', '').replace(',', '').strip())
            
            # Volume
            volume = data.get("volume", "0").replace(',', '')
            
            return {
                "lowest": low_price,
                "median": med_price,
                "volume": volume
            }
    except Exception as e:
        print(f"Error fetching price for {hash_name}: {e}")
    return None

def save_prices(current_data):
    now = datetime.now().isoformat()
    
    all_history = {}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                all_history = json.load(f)
        except json.JSONDecodeError:
            all_history = {}

    for hash_name, stats in current_data.items():
        if hash_name not in all_history:
            all_history[hash_name] = []
        
        all_history[hash_name].append({
            "timestamp": now, 
            "price": stats["lowest"],
            "median": stats["median"],
            "volume": stats["volume"]
        })
        
        if len(all_history[hash_name]) > 2200:
            all_history[hash_name] = all_history[hash_name][-2200:]

    with open(DATA_FILE, 'w') as f:
        json.dump(all_history, f, indent=2)
    
    # Update Status File
    status_data = {
        "last_fetch": now,
        "status": "Healthy",
        "cases_tracked": len(current_data),
        "total_cases_configured": len(CASES)
    }
    with open(STATUS_FILE, 'w') as f:
        json.dump(status_data, f, indent=2)

if __name__ == "__main__":
    results = {}
    for hash_name in CASES:
        stats = fetch_price(hash_name)
        if stats is not None:
            results[hash_name] = stats
            print(f"Fetched {hash_name}: Low ${stats['lowest']}, Med ${stats['median']}")
        else:
            print(f"Failed to fetch {hash_name}")
            
    if results:
        save_prices(results)
        print("Saved all updated prices.")
    else:
        # Write failure to status file
        status_data = {
            "last_fetch": datetime.now().isoformat(),
            "status": "Error: No prices fetched",
            "cases_tracked": 0,
            "total_cases_configured": len(CASES)
        }
        with open(STATUS_FILE, 'w') as f:
            json.dump(status_data, f, indent=2)
        print("No prices fetched. Updated status with error.")
