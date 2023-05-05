
import random


def main():
    play_game()
"""
play_game() function gets level from get_level funtion, generates secret answer, 
gets guess from get_guess funtion and compares it to secret answer
"""

def play_game(): 
    level = get_level()
    secret_answer = random.randint(1, level)
    
    while True:
        guess = get_guess()
        
        if guess < secret_answer:
            print("Too small!")
        elif guess > secret_answer:
            print("Too large!")
        else:
            print("Just right!")
            break
# gets level input form the user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            return level
        except ValueError:
            continue
# gets guess input form the user
def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            return guess
        except ValueError:
            continue

if __name__ == "__main__":
    main()

