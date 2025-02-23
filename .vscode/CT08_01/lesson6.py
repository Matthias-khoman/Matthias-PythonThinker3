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

quiz_scores = grade_students(student_answers, answer_key)
scores = calculate_average_score(quiz_scores)


def find_highest_score(quiz_scores):
    highest_scorers = []
    highest_score = max(quiz_scores.values())
    for students, scores in quiz_scores.items():
        if scores == highest_score:
            highest_scorers.append(students)
    return highest_scorers

print(find_highest_score(quiz_scores))
