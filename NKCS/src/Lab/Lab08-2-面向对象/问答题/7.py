class Base:
    def __init__(self):
        print('执行Base.__init__')
        self.func()

    def func(self):
        print('Base.func')

class Foo(Base):
    def __init__(self):
        print('执行Foo.__init__')
        self.func()

    def func(self):
        print('Foo.func')

f = Foo()