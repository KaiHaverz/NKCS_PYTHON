class A(object):
    @classmethod
    def f1(cls):
        print(cls)

    def f2(self):
        self.f1()

A.f1()
obj = A()
obj.f2()