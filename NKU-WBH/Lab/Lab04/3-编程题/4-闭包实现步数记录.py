# 闭包函数定义
def count_steps(original_step=0):
    total_steps = original_step
    def wrapper(new_steps):
        nonlocal total_steps
        total_steps += new_steps
        return total_steps

    return wrapper


# 执行语句
count_steps = count_steps(10)
print(count_steps(5))
print(count_steps(5))
print(count_steps(8))