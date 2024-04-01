#delee file 
import os

filename = "example.txt"
if os.path.exists(filename):#check if file exists(isfile)
    os.remove(filename)     #delete the file
    print(f"{filename} has been deleted.")
else:
    print(f"{filename} does not exist.")