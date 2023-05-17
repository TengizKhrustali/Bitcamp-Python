import re

def main():
    print(count(input("Text: ")))

def count(text):
    # Define a regular expression pattern to match "um" as a word
    pattern = r"\bum\b"
    # Find all the matches in the text, case-insensitively
    matches = re.findall(pattern, text, re.IGNORECASE)
    # Return the number of matches
    return len(matches)

if __name__ == "__main__":
    main()
