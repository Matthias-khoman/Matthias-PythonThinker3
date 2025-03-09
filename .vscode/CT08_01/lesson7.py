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

# Q1
# my_list = [87, 71, 85, 55, 77, 68, 76, 86, 56, 41, 43, 14, 5, 90, 37, 32, 60, 81, 34, 28, 29]
# n = len(my_list)
# # Debugging code
# for i in range(n):
#     for j in range(n-i-1):
#         # Change the bigger than to smaller than
#         if my_list[j] < my_list[j+1]:
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# print(my_list)

# Q2
# Points Dictionary
alpha_points = {'A' : 1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
# Making it run 5 times
num = 0
while num <= 5:
    
    word = input('What word do you want? ')
    