import re
import sys

def main():
    # Get the input from the user
    time = input("Hours: ")
    # Try to convert the input to a valid time format
    try:
        time = convert(time)
        print(time)
    except ValueError as error:
        print(error)
        sys.exit(1)

def convert(time):
    # Define a regular expression pattern to match the 12-hour format
    pattern = r"^(\d{1,2})(:\d{2})?\s(AM|PM)\sto\s(\d{1,2})(:\d{2})?\s(AM|PM)$"
    # Try to match the input time with the pattern
    match = re.match(pattern, time)
    # If there is no match, raise a ValueError
    if not match:
        raise ValueError("ValueError")
    # Extract the start and end hours, minutes, and meridiems from the match object
    start_hour = int(match.group(1))
    start_min = match.group(2) or ":00"
    start_meridiem = match.group(3)
    end_hour = int(match.group(4))
    end_min = match.group(5) or ":00"
    end_meridiem = match.group(6)
    # Validate the hours and minutes
    if not 1 <= start_hour <= 12 or not 1 <= end_hour <= 12:
        raise ValueError("ValueError")
    if not ":00" <= start_min <= ":59" or not ":00" <= end_min <= ":59":
        raise ValueError("ValueError")
    # Convert the start and end hours to 24-hour format
    if start_meridiem == "AM":
        if start_hour == 12:
            start_hour = 0
    elif start_meridiem == "PM":
        if start_hour != 12:
            start_hour += 12
    if end_meridiem == "AM":
        if end_hour == 12:
            end_hour = 0
    elif end_meridiem == "PM":
        if end_hour != 12:
            end_hour += 12

    # Format the output time as a string
    output = f"{start_hour:02d}{start_min} to {end_hour:02d}{end_min}"
    return output

if __name__ == "__main__":
    main()
