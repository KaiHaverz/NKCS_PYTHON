from functools import reduce

# 判断是否为素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 使用 filter 和 lambda 表达式求出 100 以内的素数
primes = list(filter(lambda x: is_prime(x), range(1, 101)))

# 使用 reduce 和 lambda 表达式计算这些素数的和
prime_sum = reduce(lambda x, y: x + y, primes)

print("100以内的素数:", primes)
print("100以内素数的和:", prime_sum)