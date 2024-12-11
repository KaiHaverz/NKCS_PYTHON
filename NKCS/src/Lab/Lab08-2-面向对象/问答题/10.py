class A(object):
    al = 1

    def __init__(self, num):
        self.bl = num

obj1 = A(123)
obj2 = A(555)

print(obj1.bl)
print(obj1.al)

obj1.bl = 13
obj1.al = 22

print(obj1.bl)
print(obj1.al)

print(obj2.al)
print(obj2.bl + A.al)
print(obj2.bl + obj1.al)