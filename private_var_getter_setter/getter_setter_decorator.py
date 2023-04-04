class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 20:
            raise TypeError("20 미만이어야 합니다")
        self.__age = value 

s1 = Student("kelly", 17)
print(s1.age) # 17
s1.age = 15
print(s1.age) # 15