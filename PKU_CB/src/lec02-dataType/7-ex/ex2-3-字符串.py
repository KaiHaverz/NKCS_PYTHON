name='limnku'
print(name)
print(type(name))
print(name+'pj')
print(len(name))
print(name*3)
print(name[0],name[-1])
print('lim' in name)

print("----------------")

# ASCII
print(ord('l'))
print(ord('i'))
print(ord('m'))
print(ord('A'),ord('z'))

i=0
while i<123:
    print(chr(i))
    i+=1

print("--------------------------------")

print("字符串高级功能：")
s='四川省成都市成都蓉城足球俱乐部有限公司2018'
print(len(s))
s1=s[0:19:1]
s2=s[19:23:1]
print(s1)
print(s2)

s3=s[0:23:2]
print(s3)

s4=s[23:18:-1]
print(s4)

s5=s[23:0:-1]
print(s5)

print("--------------------------------")

s6='Chengdu and Chongqing'
print(s6)
print(len(s6))
print(s6.upper())
print(s6.lower())
print(s6.split(' '))
print(s6.replace('Chongqing','Tianjin'))

print("--------------------------------")

print(s6.ljust(20))
print(s6.rjust(20))
print(s6.center(20))