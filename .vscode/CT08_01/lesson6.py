answer_key = ['A', 'B', 'B', 'D']
student_answers = {'john': ['A', 'C', 'B', 'D'],
                   'jane': ['A', 'B', 'B', 'D'],
                   'alice': ['A', 'C', 'C', 'D'],
                   'bob': ['A', 'B', 'B', 'D']}

def grade_students(student_answers: dict, answer_key: list) -> dict:
    student_score = {}
    for student, answers in student_answers.items():
        score = 0
        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                score +=1

        student_score[student] = score
    return student_score

def calculate_average_score(student_score: dict) -> float:
    total_score = 0
    for student, score in student_score.items():
        total_score = total_score + score
    average = total_score / len(student_score)

    return average

# quiz_scores = grade_students(student_answers, answer_key)
# scores = calculate_average_score(quiz_scores)

# highest score
def find_highest_score(quiz_scores):
    highest_scorers = []
    highest_score = max(quiz_scores.values())
    for students, scores in quiz_scores.items():
        if scores == highest_score:
            highest_scorers.append(students)
    return highest_scorers

# print(find_highest_score(quiz_scores))

# display results
def display_results(quiz_scores):
    if not quiz_scores:
        print('NO scores to display')
        return
    print("Class Results:")
    for student, scores in quiz_scores.items():
        print(f"{student} : {scores}")

# print(display_results(quiz_scores))

while True:
    print("Quiz Grading System Menu")
    print("1. Grade All Students")
    print("2. Calculate Class Average")
    print("3. Find Highest Scorer")
    print("4. Display All Results")
    print("5. Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        student_scores = grade_students(student_answers, answer_key)
        print("All students graded")
    elif option == 2:
        average = calculate_average_score(student_scores)
        print(average)
    elif option == 3:
        highest_scorers = find_highest_score(student_scores)
        print(highest_scorers)
    elif option == 4:
        display_results(student_scores)
    elif option == 5:
        break
    else:
        print("Not an option")

        
