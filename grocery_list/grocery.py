
# Create empty dict
grocery_list = {}

# infinite loop
while True:
    try:
        # get user input
        item = input().lower()
        # check if item is already in a dict
        if item in grocery_list:

            # if it is add 1 in the count
            grocery_list[item] += 1

        # otherwise, add item 
        else:
            grocery_list[item] = 1
    # 
    except EOFError:
        # print all items in alphabetical order
        for key in sorted(grocery_list.keys()): # sort all the items in dict into descending order
            print(grocery_list[key], key.upper()) # make item uppercase

        # stop the while loop
        break


