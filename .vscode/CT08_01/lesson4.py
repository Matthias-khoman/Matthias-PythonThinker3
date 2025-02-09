# # Exercise 1
# def greet():
#     print('Hello world')

# greet()

# Exerise 2
# def greet(name):
#     print(f'Hello {name}')

# greet('Alice')

# Exercise 3
def calculate_area(length: int | float, width: int | float) -> int | float:
    return length * width


def calculate_perimeter(length: int, width: int) -> int:
    return 2 * (length + width)


length = 6
width = 4
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
print(f'Area: {area}, perimeter: {perimeter}')