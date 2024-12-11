def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# 使用装饰器
@repeat(5)
def foo():
    print("this is foo")

# 调用 foo 函数
foo()