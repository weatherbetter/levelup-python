class Parent:
    def __init__(self):
        self.value = "Parent"
        print("Parent init")
    def test(self):
        print("Parent test")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child init")

c1 = Child()
print("--test--")
c1.test()
print("--value--")
print(c1.value)

# Parent init
# Child init
# --test--  
# Parent test
# --value--
# Parent