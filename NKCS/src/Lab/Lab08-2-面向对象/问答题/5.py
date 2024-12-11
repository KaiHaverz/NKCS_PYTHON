class Base1:
    def f1(self):
        print('base1.f1')

    def f2(self):
        print('base1.f2')

    def f3(self):
        print('base1.f3')

class Base2:
    def f1(self):
        print('base2.f1')

class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()

obj = Foo()
obj.f0()