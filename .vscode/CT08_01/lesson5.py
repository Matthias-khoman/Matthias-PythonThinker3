# Task 1
students = {"peter": [True, True, True], "lily": [False, False, True], "alice": [False, False, False], "tom": [True, True, False]}

def take_attendance(students: dict) -> dict:
    for student, attendance in students.items:
        attendance = input(f'Is {student} present(y/n)? ')
        if attendance == 'y':
            attendance = True
        elif attendance == 'n':
            attendance = False
        else:
            print('invalid input only y or n')
        students[student].append(attendance)
    print('Attendance for Class A is taken')

updated_students = take_attendance(st)

