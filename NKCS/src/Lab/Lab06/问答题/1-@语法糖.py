def get_time(func):
    def wrapper():
        func()
        print("used time: xxx")
    return wrapper

@get_time
def foo():
    print("foo")

foo()