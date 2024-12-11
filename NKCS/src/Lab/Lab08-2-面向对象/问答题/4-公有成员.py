class Dog:
    def __init__(self, name, age):
        self.name = name  # 公有属性
        self.age = age    # 公有属性

    def bark(self):  # 公有方法
        print(f"{self.name} is barking!")

dog1 = Dog("Buddy", 3)
print(dog1.name)  # 输出: Buddy
dog1.bark()       # 输出: Buddy is barking!