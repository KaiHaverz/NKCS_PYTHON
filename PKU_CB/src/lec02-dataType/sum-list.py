def sum_list(list):
    sum = 0.0
    for i in list:
        sum += i
    return sum

# 查看函数对象
print(sum_list)

my_list = [16,11,4,23,28,2,8,39,10,31,21]
my_sum = sum_list(my_list)
print("sum of my list: %d" %(my_sum),)