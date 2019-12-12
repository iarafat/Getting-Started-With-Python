from student import Student


class HighSchoolStudent(Student):

    school_name = 'PKHS'

    def get_school_name(self):
        return 'This is a High School Student'

    def get_name_capitalize(self):
        origina_value = super().get_name_capitalize()
        return origina_value + '-HS-updated'
