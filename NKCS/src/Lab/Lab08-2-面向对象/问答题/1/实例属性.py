class Dog:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # 输出: Buddy
print(dog2.name)  # 输出: Max