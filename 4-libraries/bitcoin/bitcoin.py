# Bitcoin Price Index

# Importing the sys and requests modules.
import sys
import requests

# This is a try/except block. It is trying to convert the command-line argument to a float.
# If it cannot, it will print an error message and exit the program.
try:
    n = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# This is a try/except block. It is trying to get the current price of bitcoin in USD.
# If it cannot, it will print an error message and exit the program.
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = r.json()
    # bpi is the bitcoin price index
    # USD is the currency
    # rate_float is the price of bitcoin in USD
    # data['bpi']['USD']['rate'] is a string, so we need to convert it to a float
    price = data["bpi"]["USD"]["rate_float"]
    print(f"${price * n:,.4f}")
except requests.RequestException:
    print("There was an error with the request")
    sys.exit(1)
