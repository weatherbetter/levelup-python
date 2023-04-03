class Test:
    def __init__(self, name):
        self.name = name
        print(f"init name : {self.name}")
    
    def __del__(self):
        print(f"del name : {self.name}")

test = Test("Hello")
print("----contents----")