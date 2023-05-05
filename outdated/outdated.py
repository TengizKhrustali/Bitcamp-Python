months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
# Create a loop which gets user input, splits it, converts in into YY-MM-DD
while True:
    try:
        date = input("Date: ")
        # if / is in date, using map function, split date into 3 variables and convert variables to int
        if "/" in date:
            month, day, year = map(int, date.split("/"))
        # if , is in date, split into 3 variables, add 1 to month, remove comma from day
        elif "," in date:
            date_parts = date.split()
            month = months.index(date_parts[0]) + 1
            day = int(date_parts[1].rstrip(","))
            year = int(date_parts[2])
        else:
            continue
        # print date formated properly using f string, adding 0 in front
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue
    # if none of the above is true, reprompt
    except ValueError:
        continue
