# 创建一个列表和一个元组
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)

# 将列表和元组连接
combined_list = list(my_tuple) + my_list  # 先将元组转换为列表，再进行连接
print(combined_list)  # 输出: [4, 5, 6, 1, 2, 3]

# 或者将列表转换为元组，再进行连接
combined_tuple = tuple(my_list) + my_tuple  # 先将列表转换为元组，再进行连接
print(combined_tuple)  # 输出: (1, 2, 3, 4, 5, 6)