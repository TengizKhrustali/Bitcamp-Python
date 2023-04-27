def main():
    # user input
    answer = (input("What time is it? "))
    time = convert(answer)
    match time:
        case time if time >= 7 and time <= 8:
            print("breakfast time")
        case time if 12 <= time <= 13:
            print("lunch time")
        case time if 18 <= time <= 19:
            print("dinner time")

def convert(time):
    # get hour and minute
    hours, minutes = time.split(":")
    # convert time into float
    new_minute = float(minutes) / 60
    # give converted hour to main function
    return float(hours) + new_minute
    
    
if __name__ == "__main__":
    main()
