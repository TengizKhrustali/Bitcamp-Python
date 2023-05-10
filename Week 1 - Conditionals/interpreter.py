def main():
    # get user input
    user_input = input("Expression: ")
    # print result of interpreter function, which takes user input
    print(interpreter(user_input))

def interpreter(str):
    # create a list of operators
    operators = ["+", "-", "/", "*"]
    # create a loop where if variable "operator" is in operator, so user inputs one of the operators, split by operator.
    for operator in operators:
        if operator in str:
            x, z = str.split(operator)
            z = float(z)
            x = float(x)
            # convert string into operator
            return eval(f"{x} {operator} {z}")
main()
