students = []


class Student:

    school_name = 'GPS'

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# mark = Student('Mark')
# print(mark)

# print(Student.school_name)

class HighSchoolStudent(Student):
    school_name = 'PKHS'

    def get_school_name(self):
        return 'This is a High School Student'

    def get_name_capitalize(self):
        origina_value = super().get_name_capitalize()
        return origina_value + '-HS'


james = HighSchoolStudent('james')
print(james.get_name_capitalize())























