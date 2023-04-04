class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

s1 = Student("kelly", 17)
print(s1.name) # kelly
s1.name = "stella"
print(s1.name) # stella

print(s1.__age) # AttributeError: 'Student' object has no attribute '__age'