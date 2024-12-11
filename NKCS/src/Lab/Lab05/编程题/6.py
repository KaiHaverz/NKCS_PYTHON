# 定义两个列表
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# 生成新字典
dict2 = {key: value for key, value in zip(list1, list2)}

print(dict2)