# Task 1
student_grade = {"Matthias": 98, "John": 89, "Michael": 85, "Mabel":60}
# print(f"Student grades {student_grade}")

# # Task 2
# print(f" The Grade of Matthias is {student_grade["Matthias"]}")

# # Task 3
# name = "Marc"
# grade = 100
# student_grade[name] = grade
# print(f" Students: {student_grade}")

# # Task 4
# student_grade["John"] = 10
# print(f" Students: {student_grade}")

# # Task 5
# del student_grade['John']
# print(f"Students {student_grade}")

# Task 6
# if 'Michael' in student_grade:
    # print("Michael is in the dictionary")

# Task 7
# for student in student_grade:
#     grade = student_grade[student]
#     print(f" {student} Score {grade}")
    
#     # print(student)
#     # break

# # Method 2
# for name, grade in student_grade.items():
#     print(f"{name} has a score of {grade}")

# In-Class exercise: Restaurant Menu

# Task 1: Display the menu
menu = {"Cheeseburger": 5.50,
            "Double Bacon Burger": 7.90,
            "Chicken Sandwich": 6.20,
            "Crispy Fries": 2.80,
            "Cheese Fries": 4.50,
            "Soda": 2.00}

def display_menu():
    print("{:^10}Welcome to HanBaoBao{:^10}".format('*'*10, '*'*10))
    print("{:^20}Here is the menu{:^20}".format('-'*10, '-'*10))
    for food, price in menu.items():
        print("{:^30}:${:^8.2f}".format(food, price))
    print("\n")
    print("end of menu")

customer_order = {}

def take_order(order, menu, customer):
    if order in menu:
        d
        pass 

# display_menu()