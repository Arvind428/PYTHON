# if file exists file overwrites 
# if file doesn't -w creates it
# file = open("hiaa.txt", "w")
# file.write("Hi this is api")
# file.close()


# with open("hiaa.txt", "w") as f:
#    f.write("this file is created using w")

# file = open("hiaa.txt", "r")
# print(file.read())
# file.close()

with open("hiaa.txt", "a") as f:
    f.write(" new log added\n")

# file = open("newfile1.txt", "x")
# file.write("This file is created using x mode.")
# file.close()