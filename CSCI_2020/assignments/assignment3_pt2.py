def calculate_score(student):
    assignment = student['assignment']
    assignment_min = min(assignment)
    assignment.remove(assignment_min)
    assignment_sum = sum(assignment)

    quizzes = student['Quizzes']
    quizzes_min = min(quizzes)
    quizzes.remove(quizzes_min)
    quizzes_sum = sum(quizzes)
    

    sum_grades = (assignment_sum * 0.08) + quizzes_sum + sum(student['Midterm']) + sum(student['Final'])
    
    return sum_grades


def calculate_grade(score):
    if score <= 100.00 and score >= 93.00:
        print('You got an A.')
    elif score <= 92.99 and score >= 90.00:
        print('You got a A-.')
    elif score <= 89.00 and score >= 87.00:
        print('You got an B+.')
    elif score <= 86.99 and score >= 83.00:
        print('You got a B .')
    elif score <= 82.99 and score >= 80.00:
        print('You got a B-.')
    elif score <= 79.99 and score >= 77.00:
        print('You got a C+.')
    elif score <= 76.99 and score >= 73.00:
        print('You got a C.')
    elif score <= 72.99 and score >= 70.00:
        print('You got a C-.')
    elif score <= 69.99 and score >= 67.00:
        print('You got a D+.')
    elif score <= 66.99 and score >= 60.00:
        print('You got a D.')
    else:
        print('You got an F.')


    


John = { "name":"john Adams",
 "assignment" : [90, 85, 80, 90, 100,60],
 "Quizzes" : [5, 4.5, 3.75, 4.25],
 "Midterm" : [18],
 "Final" : [23] 
}

Johns_score = calculate_score(John)
print(Johns_score)
Johns_grade = calculate_grade(Johns_score)

