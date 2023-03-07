# Create a function called Hello
def Hello(to = "World"):
    print("Hello", to)
  

# Ask for user's name
name = input("What is your name? ").strip().title()

# Call function Hello
Hello(name)
