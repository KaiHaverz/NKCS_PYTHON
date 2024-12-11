def remove_duplicates_with_dict(lst):
    return list(dict.fromkeys(lst))

# 示例
lst = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates_with_dict(lst)
print(result)