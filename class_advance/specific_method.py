class Student:
    def __init__(self, name, eng, math):
        self.name = name
        self.eng = eng
        self.math = math

    def get_sum(self):
        return self.eng + self.math
    
    def __str__(self):
        return f"{self.name} {self.get_sum()}"
    
    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스 인스턴스만 비교할 수 있다")
        return self.get_sum() == value.get_sum()
    
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()


s1 = Student("kelly", 82, 21)
s2 = Student("tella", 45, 75)
print(str(s1)) # kelly 103
print("s1 == s2", s1 == s2) # s1 == s2 False
print("s1 != s2", s1 != s2) # s1 != s2 True
print("s1 > s2", s1 > s2) # s1 > s2 False

print(isinstance(s1, Student)) # True
print(s1 == 103) # TypeError: Student 클래스 인스턴스만 비교할 수 있다
