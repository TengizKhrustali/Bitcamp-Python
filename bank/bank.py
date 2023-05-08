def main():
    
    greeting = input("Please enter a greeting: ")
    greet = value(greeting)
    print(f"${greet}")
    
def value(greeting):
    greeting = greeting.lstrip().lower()
    if "hello" in greeting:
        return (0)
    elif greeting.startswith("h"):
        return (20)
    else:
        return (100)

if __name__ == "__main__":
    main()

