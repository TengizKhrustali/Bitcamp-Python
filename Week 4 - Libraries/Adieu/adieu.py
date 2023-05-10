
import inflect

p = inflect.engine()

#make empty list named "names"
names = []

# create a loop which appends input to a list and then using inflect, separates it with commas and "and"
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        break
