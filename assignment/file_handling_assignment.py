
# Open a file named "my_file.txt" in write mode ('w')
with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1 in file creation.\n")
    file.write("0123457891112\n")
    file.write("This is python file handling assignment adding mix on nummbers.\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    contents = file.read()
    print("Contents of my_file.txt:")
    print(contents)

# File Appending
with open("my_file.txt", "a") as file:
    file.write("Appending line 4 with more text.\n")
    file.write("6568990788990\n")
    file.write("Adding another line with a mix of text and numbers.\n")

# Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Error handling operation has completed.")