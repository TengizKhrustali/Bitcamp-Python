while True: # loops forever
    # askes for input, strips input and splits it into list of two numbers
    fraction = input("Fraction: ").strip()
                
    try:
        # takes splitted two numbers, converts to int divides and multipies by 100% to get percentage
        x , y = map(int, fraction.split('/'))
        percentage = x / y * 100
        percentage = round(percentage)
        # if percentage is higher than 100 continues loop
    except (ZeroDivisionError):
        continue
    except (ValueError):
        continue
    if percentage > 100:
        continue
    elif percentage <= 1:
        print("E")
        
    elif percentage >=99:
        print("F")
        
    else:
        print(percentage, "%", sep="")
        
    break
