def get_time(func):
    def wrapper():
        func()
        print("used time: xxx")
    return wrapper

def foo():
    print("foo")

# 使用装饰器函数
foo = get_time(foo)
# 调用装饰后的函数
foo()