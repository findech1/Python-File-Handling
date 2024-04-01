#read the file then write using context managers

with open("example.txt", "r+") as file:
    contents = file.read() #read the contents fo the file
    file.write(" Chlroromethane")

class MyContexManager:
    def __enter__(self):
        print("Entering Context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Context")
        if exc_type is not None:
            print(f"An error of type {exc_type} occured:{exc_val}")
            return True
with MyContexManager() as cm:
            print("Inside context")
            #code that may raise an exception