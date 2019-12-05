students = []


def get_students_titlecase():
    titlecase = []
    for student in students:
        titlecase = student['name'].title()
    return titlecase


def print_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id=332):
    student = {'name': name, 'student_id': student_id}
    students.append(student)


def add_students():
    while True:
        student_name = input('Enter student name: ')
        student_id = input('Enter student id: ')
        if student_name == 'null' and student_id == 'null':
            break

        add_student(student_name, student_id)


print('Do you want to add students?')
answer = input('Enter Yes or No: ')

if answer.lower() == 'yes':
    add_students()

print_students_titlecase()
