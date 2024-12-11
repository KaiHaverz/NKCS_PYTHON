class Dog:
    species = "Canis familiaris"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.species)  # 输出: Canis familiaris
print(dog2.species)  # 输出: Canis familiaris