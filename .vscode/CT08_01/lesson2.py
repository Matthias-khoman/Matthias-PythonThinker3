# Task 1
student_grade = {"Matthias": 98, "John": 89, "Michael": 85}
print(f"Student grades {student_grade}")

# Task 2
print(f" The Grade of Matthias is {student_grade["Matthias"]}")

# Task 3
name = "Marc"
grade = 100
student_grade[name] = grade
print(f" Students: {student_grade}")

# Task 4
student_grade["John"] = 10
print(f" Students: {student_grade}")

# Task 5
del student_grade['John']
print(f"Students {student_grade}")

# Task 6
# if 'Michael' in student_grade:
    # print("Michael is in the dictionary")