def func(a):
    print(a)

class MyClass:
    def __init__(self,value):
        self.value=value

    def func(self):
        print(self.value)

#调用函数
func("北风毫不留情")
#创造类的实例并调用方法
obj=MyClass("把叶子吹落")
obj.func()

