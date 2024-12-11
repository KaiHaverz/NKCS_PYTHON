class A(object):
    a = 11

    def __init__(self, num):
        self.b = num

obj = A(123)
print(obj.a)
print(obj.b)
print(A.a)
print(A.b)