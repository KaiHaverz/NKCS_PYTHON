def is_prime(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):  # 只需检查到n的平方根
            if n % i == 0:
                return False
        return True

n=int(input("请输入一个数字:"))
print(is_prime(n))