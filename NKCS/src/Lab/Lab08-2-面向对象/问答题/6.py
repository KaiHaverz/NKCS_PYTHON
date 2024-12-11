class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1()
        print('base.f3')

class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()

obj2 = Foo()
obj2.f2()