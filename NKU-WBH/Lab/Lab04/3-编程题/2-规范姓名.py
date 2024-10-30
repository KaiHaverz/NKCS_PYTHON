names=['BO', 'JAZULI', 'ABUBAKAR','LIMAO',"BASIRU"]

# 使用 map 和 lambda 表达式将姓名转换为规范形式
normalized_names = list(map(lambda name: name.capitalize(), names))

print(normalized_names)