class Dog:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.age = age      # 公有属性

    def get_name(self):  # 公有方法，用于访问私有属性
        return self.__name

    def set_name(self, name):  # 公有方法，用于修改私有属性
        self.__name = name

dog1 = Dog("Buddy", 3)
print(dog1.get_name())  # 输出: Buddy
dog1.set_name("Max")
print(dog1.get_name())  # 输出: Max
# print(dog1.__name)  # 这行代码会报错，因为__name是私有属性