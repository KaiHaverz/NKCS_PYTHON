def func_out(info):
    def decorator(func):
        def wrapper():
            print(info)
            print("call function")
            return func
        return wrapper
    return decorator

@func_out(info="hello!")
def foo():
    print("this is foo")

foo()