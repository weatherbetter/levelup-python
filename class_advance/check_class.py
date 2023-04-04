class Human:
    def __init__(self):
        pass

class Student(Human):
    def __init__(self):
        pass

student = Student()
print("instance", isinstance(student, Student))
print("type", type(student) == Human)

# instance True
# type False
