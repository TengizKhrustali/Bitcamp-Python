import sys
import os
from PIL import Image, ImageOps

def main():
    # Check if the number of command-line arguments is valid
    check_argument()
    # Get the input and output file names and extensions
    input_file, output_file = check_file_name()
    # Overlay a shirt image on the input image and save it as the output image
    overlay_shirt(input_file, output_file)

# This function checks if the number of command-line arguments equals to 3, if not exit
def check_argument():
    if len(sys.argv) != 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments ")
        sys.exit(2)

# This function checks for file name extension and returns them
def check_file_name():
    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # Define a tuple of valid extensions
    extensions = (".jpg", ".jpeg", ".png")
    # split names of files into extension and the name before last dot
    input_extension = os.path.splitext(input_file)[1]
    output_extension = os.path.splitext(output_file)[1]
    # Check if either of the file names does not end with the valid extensions
    if not input_extension.lower() in extensions or not output_extension.lower() in extensions:
        # If yes, print an error message and exit the program
        print("Invalid input")
        sys.exit(3)
    # Check if the input and output have different extensions
    if input_extension != output_extension:
        print("Input and output have different extensions")
        sys.exit(4)
    # Return the file names and extensions
    return input_file, output_file

# This function overlays a shirt image on an input image and saves it as an output image
def overlay_shirt(input_file, output_file):
    try:
        # Open the input image with Image.open
        input_image = Image.open(input_file)
        # Open the shirt image with Image.open
        shirt_image = Image.open("shirt.png")
        # Resize and crop the input image to be the same size as the shirt image with ImageOps.fit
        resized_image = ImageOps.fit(input_image, shirt_image.size)
        # Overlay the shirt image on the resized image with Image.paste
        resized_image.paste(shirt_image, (0, 0), shirt_image)
        # Save the result as the output file with Image.save
        resized_image.save(output_file)
    except IOError:
        # Handle any errors that might occur when opening or saving the images
        print("Could not open or save one of the images")

if __name__ == "__main__":
    main()
