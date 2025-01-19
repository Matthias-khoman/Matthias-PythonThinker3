# Check material
# if it is plastic 
# throw in bin for plastic items
# if it is paper
# throw in bin for paper items
# if it is glass
# put in bin for glass items


# Task 1

# numbers = [1, 2, 3, 4, 5]

# def is_ascending(items):
#     i = 0 
#     for i in range(len(items) - 1):
#         if items[i] > items[i + 1]:
#            return False
        
#     return True
        
print(is_ascending(numbers))

# Task 2

list1 = [9, 6, 3, 25, 21, 8, 23, 1, 17, 14]

def bubble_sort(numbers):
    n = 0
    for n in range(len(numbers) - 1):
        if numbers[n] > numbers[n + 1]:
            temp = numbers[n + 1]
            numbers[n + 1] = numbers[n]
            numbers[n] = temp
            
        return numbers

# print(bubble_sort(list1))


n = len(list1)
def bubble_sort(numbers):
    for i in range(n):
        for j in range(0, n - i - 1):
            if list1[j] > list1[j + 1]:
                list[j] , list1[j + 1] = list1[j + 1], list1[j]
    return numbers


print(list1)