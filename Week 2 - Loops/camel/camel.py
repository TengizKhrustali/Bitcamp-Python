def main():
    # get user input of theword which is in camelCase
    camelCase = input("camelCase: ")
    # print "snake_case:" and modify print function so that new line is not printed
    print("snake_case: ", end="")
    # call change_to_snake function
    change_to_snake(camelCase)
    

def change_to_snake(word):
    # loop through every letter
    for letter in word:
        # check if letter is uppercase
        if letter.isupper():
            # if letter is uppercase, print _ symbol followed by the uppercase letter which converts to lowercase and use end="" not to print new line
            print("_" + letter.lower(), end="")
        else:
            # if letter is not uppercase, then print that letter
            print(letter, end="")
    # print new empty line when the for loop is done
    print()   
    
if __name__ == "__main__":
    main()
