import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        """
        计算圆的周长
        """
        circumference = 2 * math.pi * self.radius
        return round(circumference, 2)

    def calculate_area(self):
        """
        计算圆的面积
        """
        area = math.pi * (self.radius ** 2)
        return round(area, 2)

# 获取用户输入的半径
radius = float(input("请输入圆的半径: "))

# 创建 Circle 类的实例
circle = Circle(radius)

# 计算并输出周长和面积
print(f"圆的周长: {circle.calculate_circumference()}")
print(f"圆的面积: {circle.calculate_area()}")