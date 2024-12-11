class A(object):
    @classmethod
    def f(cls):
        print(cls)

A.f()
obj = A()
obj.f()