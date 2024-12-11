# merge sort
import random

def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    mid = int(len(data_list)/2)
    left = merge_sort(data_list[:mid])
    right = merge_sort(data_list[mid:])
    merged=[]
    while left and right:
        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    merged.extend(right if right else left)
    return merged

data_list=[random.randint(0,100) for i in range(10)]
print(data_list)
print(merge_sort(data_list))