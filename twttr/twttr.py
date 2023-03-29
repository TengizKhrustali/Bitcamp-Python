"""When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str of text or then outputs that same text but with all vowels (A, E, I, O, or U) omitted, 
whether inputted in uppercase or lowercase."""

# prompt user for input
def main():
    xxx = input("Input: ")
    print(replace_vowels(xxx))

# replace vowels
def replace_vowels(enter_text):
    vowels = "aeiouAEIOU"
    for char in enter_text:
        if char in vowels:
            enter_text = enter_text.replace(char, "")
    return enter_text


if __name__ == "__main__":
    main()
