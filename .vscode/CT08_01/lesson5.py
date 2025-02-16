# Task 1
students = {"peter": [True, True, True], "lily": [False, False, True], "alice": [False, False, False], "tom": [True, True, False]}

def take_attendance(students: dict) -> dict:
    for student, attendance in students.items():
        while True:
            attendance = input(f'Is {student} present(y/n)? ')
            if attendance == 'y':
                attendance = True
                students[student].append(attendance)
                break
            elif attendance == 'n':
                attendance = False
                students[student].append(attendance)
                break
            else:
                print('invalid input only y or n')
    print('Attendance for Class A is taken')
    return students

# updated_students = take_attendance(students)
# print(updated_students)

#Task 2
def attendance_percent(student: str, students: dict) -> float:
    if student in students:
        attendance_list = students[student]
        num = attendance_list.count(True)
        denom = len(attendance_list)
        return round((num / denom) * 100, 2)
    else:
        print("HEY YOU ARE NOT MY STUDENT")
    
value = attendance_percent("lily", students)
print(value)

#Task 3
def notify_low_attendance_students(students: dict, threshold: float) -> list:
    low_attendance_students = []
    for student in students.keys():
       attendance_percentage=attendance_percent(student, students)
       if attendance_percentage < threshold:
           low_attendance_students.append(student)
           print(f'{student} has low attendance
    return low_attendance_students

students_with_low_attendance = notify_low_attendance_students(students, 50)
print(students_with_low_attendance)