def decorator(func):
    def wrapper(*args):
        print("call function")
        return func(*args)
    return wrapper

@decorator
def foo(*args):
    print("this is foo")
    print(args)

foo(1,2,3)