students = []


def get_students_titlecase():
    titlecase = []
    for student in students:
        titlecase.append(student['name'].title())
    return titlecase


def print_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id=332):
    student = {'name': name, 'student_id': student_id}
    students.append(student)


def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + "\n")
        f.close()
    except Exception:
        print('Could not save file')


def read_file():
    try:
        f = open('students.txt', 'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('Could not read file')


def add_students():
    while True:
        student_name = input('Enter student name: ')
        student_id = input('Enter student id: ')
        if student_name == 'null' and student_id == 'null':
            break
        add_student(student_name, student_id)
        save_file(student_name)


print('Do you want to add students?')
answer = input('Enter Yes or No: ')

if answer.lower() == 'yes':
    add_students()

add_students()
read_file()
