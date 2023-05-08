import random

def main():
    # gets level from get_level function and stores in level variable
    level = get_level()
    # get problems from generate_problems function and store it into variable
    math_problems = generate_problems(level)
    # initialize score to 0
    score = 0
    # loop through math problems 
    for problem in math_problems:
        for i in range(3):
            answer = get_guess(problem)
            if answer == problem['answer']:
                score += 1
                break
            elif i == 2:
                print(f"EEE, the correct answer was {problem['answer']}")
            else:
                print("EEE")
    print(f"Number of problems correct: {score}")
# this function prompts user for level and returns level variable
def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError("Invalid level")
        except ValueError:
            print("Invalid level")
    
# this function grabs level number from level variable.
def generate_problems(level):
    try:
        # create digits variable and store level number
        if level == 1:
            digits = 1
        elif level == 2:
            digits = 2
        else:
            digits = 3
        # create empty list
        problems = []
        # generate 10 random problems according to level specified
        for _ in range(10):
            if digits == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            elif digits == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
            else:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
            # generate answers of problems
            answer = x + y
            # create a dictionary of x , y and their sum
            problem = {'x': x, 'y': y, 'answer': answer}
            # add the dictionary to empty list of problems
            problems.append(problem)
        return problems
    except ValueError as exc:
        raise ValueError("Invalid level") from exc

def get_guess(problem):
    while True:
        try:
            # prompt user to answer problem
            guess = int(input(f"{problem['x']} + {problem['y']} = "))
            return guess
        except ValueError:
            print("EEE")

if __name__ == "__main__":
    main()
