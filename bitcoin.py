import requests
import sys

if len(sys.argv) != 2 :
    sys.exit("missing command line argument")
 
try:
        amount = float(sys.argv[1])
except ValueError:
        sys.exit("command line argument is not a number")
url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey"

try:
    response = requests.get(url)
except requests.RequestException:
    sys.exit(" request failed ")

data = response.json()
print(data)
price = float(data['data']["priceUsd"])

total = amount*price 

print(f"${total:,.4f}")