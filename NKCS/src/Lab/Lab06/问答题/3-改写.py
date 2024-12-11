def decorator(func):
    def wrapper(*args, **kwargs):
        print("call function")
        return func(*args, **kwargs)
    return wrapper

@decorator
def foo(*args, **kwargs):
    print("this is foo")
    print("args:", args)
    print("kwargs:", kwargs)

# 调用 foo 函数
foo(1, 2, 3, a=4, b=5)