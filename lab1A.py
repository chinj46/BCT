import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

# Set up API key and endpoint
api_key = "UU2DBSVIQGEX4KIRSRE5K1QKWMQJFVSWME"
etherscan_api_url = "https://api.etherscan.io/api"

# Function to get transaction details
def get_transaction_details(tx_hash):
    params = {
        "module": "proxy",
        "action": "eth_getTransactionByHash",
        "txhash": tx_hash,
        "apikey": api_key,
    }
    response = requests.get(etherscan_api_url, params=params)
    return response.json()

# Function to perform statistical analysis (using synthetic data)
def perform_statistical_analysis():
    # Generating synthetic example data with 7-8 data points
    account_times = [datetime(2023, 1, 1, 10, 30)]
    ether_values = [2.5]
    gas_paid_values = [0.02]
    transaction_hashes = ["0x8b2a240c889d1d9b1e6c0a57ab8029b5858517b7e54a5cc2f4a9c6036a440a9c"]

    # Generate additional data points
    for _ in range(7):
        account_time = account_times[-1] + timedelta(days=random.randint(1, 7))
        account_times.append(account_time)
        ether_values.append(random.uniform(1.5, 3.5))
        gas_paid_values.append(random.uniform(0.01, 0.05))

        # Get transaction details for the current time unit
        transaction_details = get_transaction_details(transaction_hashes[-1])
        print(f"Transaction Details for {account_time}: {transaction_details}")

        # For demonstration purposes, add a new synthetic transaction hash for the next time unit
        transaction_hashes.append("0x" + ''.join(random.choice('abcdef0123456789') for _ in range(64)))

    return {"account_times": account_times, "ether_values": ether_values, "gas_paid_values": gas_paid_values}

# Function to plot data
def plot_data(x, y, xlabel, ylabel, title):
    plt.plot(x, y, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

# Main function
def main():
    # Perform statistical analysis (using synthetic data)
    statistical_results = perform_statistical_analysis()

    # Extract data for plotting
    account_times = statistical_results['account_times']
    ether_values = statistical_results['ether_values']
    gas_paid_values = statistical_results['gas_paid_values']

    # Plot data
    plot_data(account_times, ether_values, "Account Time", "Ether(ETH) Value", "Account Time vs Ether(ETH) Value")
    plot_data(account_times, gas_paid_values, "Account Time", "Gas Paid (in ETH)", "Account Time vs Gas Paid (in ETH)")

if __name__ == "__main__":
    main()
    
    !pip install requests

import requests
import json

url = "https://api.etherscan.io/api"

api_key = "UU2DBSVIQGEX4KIRSRE5K1QKWMQJFVSWME"

address = "0x388C818CA8B9251b393131C08a736A67ccB19297"

payload = {
    "module": "account",
    "action": "txlist",
    "address": address,
    "startblock": 0,
    "endblock": 99999999,
    "sort": "asc",
    "apikey": api_key
}

response = requests.get(url, params=payload)

data = json.loads(response.content)

for transaction in data['result']:
    print(transaction)
