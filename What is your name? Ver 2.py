# Define Input
name = input('What is your name? ').strip().title()


# Check if name = Joe or Torvin, if not, default greeting, if yes, personal greetings
if name != 'Joe':
  if name != 'Torvin':
    print(f"Hello, Nice to Meet You! {name}")
if name == 'Joe':
  print("HOWDY, Joe!")
if name == 'Torvin':
  print("Good Morning, Torvin!")
