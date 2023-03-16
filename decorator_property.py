class XY:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.z = 50

    @property
    def x(self):
        return self._x


temp = XY(10, 4)
print(temp.x) # 10
# temp.x = 20 # AttributeError: can't set attribute

print(temp.z) # 50
temp.z = 30
print(temp.z) # 30

print(temp._y) # 4
temp._y = 30
print(temp._y) # 30