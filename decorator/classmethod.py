class Student:
    count = 0
    students = []

    @classmethod
    def print_all(cls):
        for student in cls.students:
            print(str(student))
    
    def __init__(self, name, eng, math):
        self.name = name
        self.eng = eng
        self.math = math
        Student.count += 1
        Student.students.append(self)

    def __str__(self):
        return f"{self.name} {self.eng} {self.math}"
    
Student("kelly", 23, 82)
Student("Hell", 45, 90)

Student.print_all()
""" 
kelly 23 82
Hell 45 90
"""