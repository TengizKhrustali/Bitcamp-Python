# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
# case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

File_Name = input("tell me your file name and format ")

if File_Name.endswith(".jpg") or File_Name.endswith(".jpeg"):
    print("image/jpg")
elif File_Name.endswith(".gif"):
    print("image/gif")
elif File_Name.endswith(".png"):
    print("image/png")
elif File_Name.endswith(".pdf"):
    print("application/pdf")
elif File_Name.endswith(".txt"):
    print("application/txt")
elif File_Name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

