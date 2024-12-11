class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):  # 静态方法
        return age >= 1

print(Dog.is_adult(3))  # 输出: True