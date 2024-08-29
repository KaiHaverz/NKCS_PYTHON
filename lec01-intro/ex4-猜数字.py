import random

secret = random.randint(1, 100)
print('''这是一个猜数字游戏，
我想了一个 1-100 之间的整数，你最多可以猜六次，
试试你能猜出来吗？
''')

tries = 1
while tries <= 6:
    guess = int(input("这是你的第 %d 次机会，请输入一个 1-100 之间的整数：" %(tries,)))
    if guess == secret:
        print("恭喜你！👏在第 %d 答对了！\n 正确答案是 %d !" %(tries, secret))
        break
    elif guess > secret:
        print("Oops...你猜的数字大了一点😭")
    else:
        print("Oops...你猜的数字小了一点😭")
    tries += 1

else:
    print('''
\nOh my god!
怎么六次都没猜中，
正确答案是 %d,
再来一次吧！💪''' %(secret,))