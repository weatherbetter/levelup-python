class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} init")
    
    def __del__(self):
        print(f"{self.name} del")

Test("A")
b = Test("B")
Test("C")

# A init
# A del
# B init
# C init
# C del
# B del
