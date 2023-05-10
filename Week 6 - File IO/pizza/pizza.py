import sys
import csv
from tabulate import tabulate

def main():
    check_argument()
    file_name = check_file_name()
    output_table(file_name)

def check_argument():
    # Check if exactly one command-line argument is given, if not exit
    if len(sys.argv) != 2:
        print("Too few command-line arguments")
        sys.exit(1)

def check_file_name():
    # Check if the argument ends with .py, if not exit
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        print("not a CSV file")
        sys.exit(2)
    return filename

def output_table(filename):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            # get the first row as headers
            headers = next(reader)
            # get the rest of the rows as data
            data = list(reader)
            print(tabulate(data, headers=headers, tablefmt="grid", stralign="left"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(3)

if __name__ == "__main__":
    main()
