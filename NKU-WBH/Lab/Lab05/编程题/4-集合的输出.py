s1 = {32, 5, 'c', '32', '11'}
s2 = set({32, '46', 32, 'aa'})
s3 = set('4,32,46,11,32')
s4 = set([1, 2, 3])
s5 = set((1, 2, 3))  # 修正全角空格
s6 = set({'a': 1, 'b': 2, 'c': 3})


print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)