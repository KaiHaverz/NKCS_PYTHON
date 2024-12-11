def f_a(func):
    print("f_a")

    def w_a():
        print(1)
        func()
    return w_a

def f_b(func):
    print("f_b")
    def w_b():
        print(2)
        func()
    return w_b

@f_a
@f_b
def f_c():
    print("f_c")
    print(3)

f_c()