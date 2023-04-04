class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, value):
        if value > 20:
            raise TypeError("20 미만이어야 합니다")
        self.__age = value 

s1 = Student("kelly", 17)
# print(s1.__age) # AttributeError: 'Student' object has no attribute '__age'
print(s1.get_age()) # 17
s1.set_age(12)
print(s1.get_age()) # 12

print(s1.name) # kelly
s1.name = "stella"
print(s1.name) # stella