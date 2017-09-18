from Person import Person

class Student(Person):
    '''A class representing a student, created by inheritance
    inheriting attributes/methods from person and only extending
    the ones we need to make this a student
    '''
    def __init__(self, firstname, lastname, age, student_num, gpa):
        '''(Student, str, str, int, age, str, float) -> NoneType
        '''
        Person.__init__(self, firstname, lastname, age)
        self._student_num = student_num
        self._gpa = gpa

    def __str__(self):
        '''(Student) -> NoneType
        Return a string representing this student
        '''
        result = Person.__str__(self) + ", " + self._student_num + ", gpa: " + str(self._gpa)
        if(self._gpa >= 3.8):
            result += " (honors list)"
        return result

    def set_gpa(self, gpa):
        '''(Student, float) -> NoneType
        Set the student's GPA
        '''
        self._gpa = gpa

if (__name__ == "__main__"):
    alice = Student("Alice", "Alicson", 20, "1234", 3.5)
    print(alice)
    alice.set_age(22)
    alice.set_gpa(3.9)
    print(alice)   

