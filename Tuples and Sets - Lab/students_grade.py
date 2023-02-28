n = int(input())
student_strings = [input() for _ in range(n)]
students_dict = {}

for student_string in student_strings:
    student, grade_string = student_string.split(' ')
    grade = float(grade_string)
    if student not in students_dict:
        students_dict[student] = []

    students_dict[student].append(grade)

for student, grades in students_dict.items():
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    average_grade = sum(students_dict[student]) / len(students_dict[student])
    print(f"{student} -> {grades_formatted} (avg: {average_grade:.2f})")