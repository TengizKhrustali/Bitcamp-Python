from validators import email


def main():
    # Prompt the user for an email address
    address = input("What's your email address? ")
    # Validate the email address using the email function
    valid = email(address)
    # Print Valid or Invalid depending on the result
    if valid:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    
    main()
