# This program prompts user for bill anount and tip rate, caluclates tip amount and total amount
# and if user enters something other than a number, it prompts Please enter a valid number for the bill amount.

while True:
    bill_amount_input = input("Enter the bill amount: $")
    if bill_amount_input.isnumeric() or (bill_amount_input[0] == '-' and bill_amount_input[1:].isnumeric()):
        bill_amount = float(bill_amount_input)
        break
    else:
        print("Please enter a valid number for the bill amount.")
tip_amount = int(input("Enter the tip amount (as a whole number): "))
tip_rate = tip_amount / 100
tip_amount = bill_amount * tip_rate
total_amount = bill_amount + tip_amount
print("Tip amount: ${:.2f}".format(tip_amount))
print("Total amount: ${:.2f}".format(total_amount))

