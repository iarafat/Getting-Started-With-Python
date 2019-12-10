students = []


class Student:
    def __init__(self, name, student_id=332):
        student1 = {'name': name, 'student_id': student_id}
        students.append(student1)

    def __str__(self):
        return "Student"


mark = Student('Mark updated')
print(mark)

