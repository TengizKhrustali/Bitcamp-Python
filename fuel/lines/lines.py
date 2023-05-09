import sys

def main():
    check_argument()
    file_name = check_file_name()
    count_lines(file_name)

def check_argument():
    # Check if exactly one command-line argument is given
    if len(sys.argv) != 2:
        print("Too few command-line arguments")
        sys.exit(1)
def check_file_name():
    # Check if the argument ends with .py
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        print("not a Python file")
        sys.exit(2)
    return filename
def count_lines(filename):
    # Try to open the file and count the lines of code
    try:
        with open(filename) as file:
            lines = 0
            for line in file:
                # Strip whitespace from the line
                line = line.strip()
                # Check if the line is not empty and not a comment
                if line and not line.startswith("#"):
                    lines += 1
            print(f"Lines of code: {lines}")
    # if file does not exist, raise error and exit
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(3)
if __name__ == "__main__":
    main()   



