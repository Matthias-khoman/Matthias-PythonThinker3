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
    num_true = 0
    if student in students:
        for attendance in students[student]:
            while True:
                if attendance == True:
                    num_true +=1
                    break
            total = atten

            
        

