answer_key = ['A', 'B', 'C', 'D']
student_answers = {'john': ['A', 'C', 'B', 'D'],
                   'jane': ['A', 'B', 'B', 'D'],
                   'alice': ['A', 'C', 'C', 'D'],
                   'bob': ['A', 'B', 'B', 'D']}

def grade_students(student_answers: dict, answer_key: list):
    student_score = {}
    for student, answers in student_answers.items():
        score = 0
        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                score +=1

        stude
