import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 3 and sys.argv[1] == "-f":
    figlet.setFont(font=sys.argv[2])
elif len(sys.argv) != 1:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
