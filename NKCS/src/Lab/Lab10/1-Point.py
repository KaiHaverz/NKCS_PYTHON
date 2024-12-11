# 运算符重载

class Point:
    # 初始化，定义类，x，y两种属性
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 重载加法运算符
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # 重载减法运算符
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # 重载字符串表示方法，方便打印
    def __str__(self):
        return f'({self.x}, {self.y})'


p1=Point(1,2)
p2=Point(3,4)

print(p1 + p2)
print(p1 - p2)