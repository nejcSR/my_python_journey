import requests
import csv
import time
from datetime import datetime

# List of coins to track
COINS = ["bitcoin", "ethereum", "dogecoin"]
# Currency to track prices in
CURRENCY = "eur"
# File where prices are logged
FILENAME = "crypto_prices.csv"

# Define alerts as a list of tuples: (coin_name, condition, threshold)
# condition can be "above" or "below"
ALERTS = [
    ("bitcoin", "above", 30000),
    ("ethereum", "below", 1500),
    ("dogecoin", "above", 0.3),
]

def fetch_prices(coins, currency):
    """Fetch prices for multiple coins from CoinGecko API"""
    ids = ",".join(coins)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # parse JSON response into dict
        return data
    else:
        print("Error fetching price:", response.status_code)
        return None

def log_prices(prices, filename=FILENAME):
    """Append current prices with timestamp to CSV file"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline="") as file:
        writer = csv.writer(file)
        # Create row: timestamp + prices for each coin
        row = [now] + [prices[coin][CURRENCY] for coin in COINS]
        writer.writerow(row)
    # Print logged prices summary to console
    print(f"Logged prices at {now}: " + ", ".join([f"{coin}={prices[coin][CURRENCY]}" for coin in COINS]))

def check_alerts(prices):
    """Check price alerts and print if conditions met"""
    for coin, condition, threshold in ALERTS:
        # Safely get price, handle if coin not in prices dict
        price = prices.get(coin, {}).get(CURRENCY)
        if price is None:
            continue  # skip if data missing
        if condition == "above" and price > threshold:
            print(f"ALERT: {coin} price is above {threshold} ({price})")
        elif condition == "below" and price < threshold:
            print(f"ALERT: {coin} price is below {threshold} ({price})")

def main():
    prices = fetch_prices(COINS, CURRENCY)
    if prices:
        log_prices(prices, FILENAME)
        check_alerts(prices)

if __name__ == "__main__":
    while True:
        main()  # fetch, log, and alert
        time.sleep(300)  # wait 5 minutes before next fetch
