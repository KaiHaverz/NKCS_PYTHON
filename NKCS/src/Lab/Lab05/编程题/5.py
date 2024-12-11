values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 200, 230, 330]

# 初始化字典
result = {'k1': [], 'k2': []}

# 遍历集合，按条件保存值
for value in values:
    if value > 66:
        result['k1'].append(value)
    else:
        result['k2'].append(value)

print(result)