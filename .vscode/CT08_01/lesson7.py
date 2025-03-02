import os 
# Exercise 0
filepath = os.getcwd()

fullpath = os.path.join(filepath, "example.txt")

if os.path.exists(fullpath):
    print("{} exist".format(fullpath))
else:
    print("{} does not exist".format(fullpath))

# Exercise 1
file = open(fullpath, "w")
file.write("Hello John")
file.close()

# Exercise 2
file = open(fullpath, "r")
