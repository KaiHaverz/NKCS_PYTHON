def func():
    print("CDXQ!")

func()

import time

def time_counter(f):
    start=time.time()
    f()
    end=time.time()
    return (end-start)


time_counter(func)


def func1():
    pass
def func2():
    pass
def func3():
    pass
def func4():
    pass

print("----------------------")
def time_counter1(f):
    def wrapper():
        start=time.time()
        f()
        end=time.time()
        return (end-start)

    return wrapper

func=time_counter1(func)
func()

@time_counter1
def func5():
    print("我是第五个函数")
func5()


from datetime import datetime,timezone
def logger(f):
    def inner(*args,**kwargs):
        called_at=datetime.now()
        to_execute=f(*args,**kwargs)
        print(f"{f.__name__} executed Logged at {called_at}")
        return to_execute

    return inner

@logger
def func6():
    pass
func6()

print("----------------------")

def foo(x):



