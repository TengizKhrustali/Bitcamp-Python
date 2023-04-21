def main():
    
    while True: # loops forever
        # strips input and splits it into two numbers
        fraction = (input("Fraction: ")).strip().split("/") 

        try:
            # takes two numbers, converts to int divides and multipies by 100% to get percentage
            percentage = int(int(fraction[0])/int(fraction[1])*100)

            if percentage > 100:
                pass
            elif percentage <= 1:
                print("E")
            elif percentage >=99:
                print("F")
            else:
                print(percentage, "%", sep="")
        
        except ZeroDivisionError:
            print("Cant devide by zero;")
        except ValueError:
            print("Invalid fraction;")
    
if __name__ == "__main__":
    main()

