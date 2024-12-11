class Dog:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.age = age      # 实例属性

    def get_name(self):
        return self.__name

dog1 = Dog("Buddy", 3)
print(dog1.get_name())  # 输出: Buddy
# print(dog1.__name)  # 这行代码会报错，因为__name是私有属性