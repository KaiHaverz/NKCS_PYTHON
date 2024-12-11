height = 99.9
mt = everest = "佘山"
print(height)
print(mt)
print(everest)
print(type(height))
print(type(mt))
print(type(everest))

print("------------------------------------")
name = '重庆市铜梁区铜梁龙足球俱乐部有限公司'
print(name[0:18:1])
print(name[0:18:2])

print("------------------------------------")

print(name*2)
print(mt+name)
print(mt==name)

print("------------------------------------")

print('铜梁龙' in name)

print("\n字符串高级操作")
s1 = 'PJ i love u'
print(s1.split(' '))

print('_'.join(["Chengdu","Yongyuan","de","Hong"]))

print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.replace('PJ','Chiharu.Shida'))