#open file for reading
file = open("expiredItems.csv", "r")

#Read the contents
content = file.read()

#Print the content
print(content)

#close file
file.close()