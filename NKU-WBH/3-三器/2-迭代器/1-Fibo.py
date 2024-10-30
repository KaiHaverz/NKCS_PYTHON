def fibo(max):
    n,a,b = 0,1,1
    while n < max:
        a,b = b,a+b
        n+=1
    return "done"

fibo(1)