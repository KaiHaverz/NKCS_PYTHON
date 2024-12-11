class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):  # 实例方法
        print(f"{self.name} is barking!")

dog1 = Dog("Buddy", 3)
dog1.bark()  # 输出: Buddy is barking!