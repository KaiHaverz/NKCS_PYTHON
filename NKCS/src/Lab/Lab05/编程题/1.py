def find_special_number(lst):
    for i in range(len(lst)):
        if (i == 0 or lst[i] > max(lst[:i])) and (i == len(lst) - 1 or lst[i] < min(lst[i + 1:])):
            return i
    return -1

# 示例1
lst1 = [6, 3, 4, 9, 1]
result1 = find_special_number(lst1)
print(result1)

# 示例2
lst2 = [4, 3, 6, 9, 7]
result2 = find_special_number(lst2)
print(result2)