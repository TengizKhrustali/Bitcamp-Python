import sys
import requests

def main():
    check_commandline()
    bitcoins = convert_to_float()
    response = get_price()
    extract_and_print(response, bitcoins)

def check_commandline():
    # checks if the number of command-line arguments is not equal to 2. If it is not equal to 2, print error message and exit
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

def convert_to_float():
    # convert the second command-line argument to a float. If it cannot be converted to a float, print error and exit
    try:     
        bitcoins = float(sys.argv[1])
        return bitcoins
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
def get_price():
    # get price, if the response status code is not equal to 200 (OK), it prints an error message and exits the program 
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching bitcoin price")
        sys.exit(1)
    else:
        return response
def extract_and_print(response, bitcoins):
    # extract the current Bitcoin price from the JSON response returned by the API and calculate the cost of buying the specified number of Bitcoins.
    data = response.json()
    rate = data["bpi"]["USD"]["rate_float"]
    cost = rate * bitcoins

    # print cost of buying the specified number of Bitcoins in USD, formatted with commas as thousands separators and rounded to four decimal places.
    print(f"Cost of {bitcoins:,} bitcoins: ${cost:,.4f}")

if __name__ == "__main__":
    main()
