# import os 
# # Exercise 0
# filepath = os.getcwd()

# fullpath = os.path.join(filepath, "example.txt")

# if os.path.exists(fullpath):
#     print("{} exist".format(fullpath))
# else:
#     print("{} does not exist".format(fullpath))

# # Exercise 1
# file = open(fullpath, "w")
# file.write("Hello John")
# file.close()

# # Exercise 2
# file = open(fullpath, "r")
# content = file.read()
# print(f'File Content {content}')
# file.close()

# # Exercise 3
# with open(fullpath, 'r') as file:
#     content = file.read()
#     print(f"File content with 'with': {content}")

# # Exercise 4
# with open(fullpath, "a") as file:
#     file.write("\nThis is John")
#     file.write("\nThis is John Doe")

# # Exercise 5
# lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
# with open(fullpath, "w") as file:
#     file.writelines(lines)

# with open(fullpath, "r") as file:
#     lines = file.readline()


my_list = [5, 8, 10, 9, 11, 12, 15, 2]
n = len(my_list)
# Debugging code
for i in range(n):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)
    