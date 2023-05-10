def main():
    # user input
    user_time = convert((input("What time is it? ")))
    if 7 <= user_time <= 8:
        print("Breakfast time")
    elif 12 <= user_time <= 13:
        print("Lunch time")
    elif 18 <= user_time <= 19:
        print("Dinner time")

def convert(time):
    if time[len(time)-4:] == "p.m.":
        time = time[:-4]
        hours, minutes, = time.split(":")
        hours = float(hours) + 12
    else:
        if time[len(time)-4:] == "a.m.":
            time = time[:-4]
        hours, minutes = time.split(":")
            # convert time into float
    new_time = float(hours) + float(minutes)/60
    return new_time

if __name__ == "__main__":
    main()
