import re

def main():
    # Use the code you provided in the main function
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regular expression for IPv4 address
    pat = re.compile(
        "^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
        )
    # Try to match the IP string with the regular expression and return the boolean value
    return bool(pat.match(ip))

if __name__ == "__main__":
    main()
