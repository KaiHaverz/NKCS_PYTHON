cars = [(1, 'byd'), (3, 'xiaopeng'), (2, 'tesla'), (4, 'weilia')]

# 使用 sorted 和 lambda 表达式按照排名进行排序
sorted_cars = sorted(cars, key=lambda x: x[0])

print(sorted_cars)