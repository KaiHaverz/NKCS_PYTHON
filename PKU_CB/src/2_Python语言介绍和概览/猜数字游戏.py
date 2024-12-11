import random

secret=random.randint(1,100)
print('''猜数字游戏！
你有6次机会，看看你能否猜出来''')

tries=1
while tries<=6:
    guess=int