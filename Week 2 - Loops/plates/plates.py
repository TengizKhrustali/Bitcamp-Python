"""
ASSIGNMENT:
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”    “No periods, spaces, or punctuation marks are allowed.”

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # vanity plates length must be max 6 characters and min 2 characters
    if len(s) < 2 or len(s) > 6: #if statement, if length of s is less than 2 and greater than 6 return false
        return False

    # All vanity plates must start with at least two letters
    if not s[0:2].isalpha(): # if chracter 0 and 1 in plate are numbers, return false
        return False
    
    # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
    # The first number used cannot be a ‘0’
    
    for i in s:
        if i.isdigit():
            index = s.index(i)
            if s[index:].isdigit() and i != "0":
                return True
            else:
                return False
    
    # No periods, spaces, or punctuation marks are allowed
    if not s.isalnum(): # if plate is not alphanumeric, return false
        return False
    
    return True

if __name__ == "__main__":
    main()
