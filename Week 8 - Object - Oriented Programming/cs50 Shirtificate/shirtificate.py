# Import the fpdf2 module
from fpdf import FPDF, XPos, YPos

# Define some constants for the PDF dimensions and margins
PDF_WIDTH = 210 # A4 width in mm
PDF_HEIGHT = 297 # A4 height in mm
MARGIN = 10 # Margin in mm

# Define some constants for the shirt image dimensions and position
SHIRT_WIDTH = 150 # Shirt width in mm
SHIRT_HEIGHT = 150 # Shirt height in mm
SHIRT_X = (PDF_WIDTH - SHIRT_WIDTH) / 2 # Shirt x coordinate (centered horizontally)
SHIRT_Y = 100 # Shirt y coordinate (arbitrary)

# Define some constants for the text font, size and color
FONT = "Helvetica" # Font name
SIZE = 24 # Font size in pt
COLOR = (255, 255, 255) # Font color in RGB (white)

# Create a new FPDF object with portrait orientation and A4 format
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Disable automatic page break
pdf.set_auto_page_break(False)

# Add a new page to the PDF
pdf.add_page()

# Set the font for the header text
pdf.set_font(FONT, size=SIZE)

# Set the text color to black
pdf.set_text_color(0, 0, 0)

# Write the header text "CS50 Shirtificate" centered horizontally at the top of the page
pdf.cell(w=0, h=SIZE, txt="CS50 Shirtificate", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

# Load the shirt image from the file
pdf.image("shirtificate.png", x=SHIRT_X, y=SHIRT_Y, w=SHIRT_WIDTH, h=SHIRT_HEIGHT)

# Prompt the user for their name
name = input("Name: ")

# Set the font for the name text
pdf.set_font(FONT, size=SIZE)

# Set the text color to white
pdf.set_text_color(*COLOR)

# Calculate the width of the name text in mm
name_width = pdf.get_string_width(name)

# Calculate the x coordinate of the name text (centered horizontally over the shirt image)
name_x = SHIRT_X + (SHIRT_WIDTH - name_width) / 2

# Calculate the y coordinate of the name text (arbitrary)
name_y = SHIRT_Y + SHIRT_HEIGHT / 2

# Write the name text over the shirt image
pdf.text(x=name_x, y=name_y, txt=name)

# Output the PDF to a file called "shirtificate.pdf"
pdf.output("shirtificate.pdf")
