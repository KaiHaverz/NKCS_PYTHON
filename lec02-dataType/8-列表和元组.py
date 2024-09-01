import math

print([])
print(list())

starting_shirt_num=[16,11,4,23,28,2,8,39,10,21,31]
print(starting_shirt_num)

substitutes_shirt_num=[1,22,27,36,3,15,6,7]
print(substitutes_shirt_num)

shirt_num = starting_shirt_num + substitutes_shirt_num
print(shirt_num)

print(len(shirt_num))
print(shirt_num[0])

print("---------------------")

for i in range(0,len(shirt_num)):
    print(shirt_num[i])
    i+=1

print("---------------------")

shirt_num.insert(19,33)
print(shirt_num)
shirt_num.remove(33)
print(shirt_num)
shirt_num.sort()
print(shirt_num)

print("---------------------")

print(31 in shirt_num)
print(shirt_num.index(31))
print(sum(shirt_num))