# prompt user for input
def main():
    text = input("Input: ")
    print(shorten(text))

# replace vowels
def shorten(word):
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            word = word.replace(char, "")
    return word

if __name__ == "__main__":
    main()
