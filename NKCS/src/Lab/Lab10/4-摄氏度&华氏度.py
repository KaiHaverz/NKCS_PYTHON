# 摄氏度类
class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

# 华氏度类
class Fahrenheit:
    def __get__(self, instance, owner):
        # 从摄氏度转换为华氏度
        return instance.cel * 9/5 + 32

    def __set__(self, instance, value):
        # 从华氏度转换为摄氏度
        instance.cel = (float(value) - 32) * 5/9

# 描述符类
class Temperature:
    cel = Celsius()
    f = Fahrenheit()

# 测试代码
temp = Temperature()  # temp为描述符类实例
print(temp.cel)  # 可以查看摄氏度的值
print(temp.f)  # 并且可以直接计算出华氏度

temp.cel = 37.8  # 设置摄氏度的值
print(temp.f)  # 依据该值可计算出华氏度