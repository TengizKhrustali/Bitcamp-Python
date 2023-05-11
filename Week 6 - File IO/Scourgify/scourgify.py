# priovde two command-line arguments
# split name into first and last name

import sys
import csv


def main():
    check_argument()
    file_name = check_file_name()
    output_table(file_name)
# this function checks if command-line arg equals to 3, if not exit
def check_argument():
    if len(sys.argv) != 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments ")
        sys.exit(2)
# this function checks for file name and if it does not end with .csv, exits, if yes returns filename
def check_file_name():
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        print("Could not read", filename)
        sys.exit(3)
    return filename
# this function gets content from a file, edits it and writes in new file
def output_table(file_name):
    try:
        # open the file
        with open(file_name, "r") as infile:
            reader = csv.DictReader(infile)
            # Get the output file name from the user input
            output_file = sys.argv[2]
            # opens file with the given name in read mode
            with open(output_file, "w") as outfile:
                # creates a csv.DictWriter object and assigns it to the variable writer
                writer = csv.DictWriter(outfile, fieldnames=["first","last", "house"])
                writer.writeheader()
                for row in reader:
                    # Split the name into first and last
                    first, last = row["name"].strip().split(", ")
                    # Write the new row with the new order, swap the order of the first and last names 
                    writer.writerow({
                        "last": first, 
                        "first": last, 
                        "house": row["house"]
                        })

    except FileNotFoundError:
        sys.exit(4)

if __name__ == "__main__":
    main()
