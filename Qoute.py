# The program asks user to enter author of the qoute and prints the qoute.


Author = input("Who said it? ")
quotes = {"Naruto": "Never give up!", "Albert Einstein": "Creativity is seeing what others see and thinking what no one else ever thought!"}

if Author in quotes:
    print(f'{Author} says, "{quotes[Author]}"')



 
