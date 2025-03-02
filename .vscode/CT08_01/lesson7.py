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
content = file.read()
print(f'File Content {content}')
file.close()

# Exercise 3
with open(fullpath, 'r') as file:
    content = file.read()
    print(f"File content with 'with': {content}")

# Exercise 4
with open(fullpath, "a") as file:
    file.write("\nThis is John")
    file.write("\nThis is John Doe")

# Exercise 5
