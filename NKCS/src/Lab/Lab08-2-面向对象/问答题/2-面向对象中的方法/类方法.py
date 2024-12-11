class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):  # 类方法
        return cls.species

print(Dog.get_species())  # 输出: Canis familiaris