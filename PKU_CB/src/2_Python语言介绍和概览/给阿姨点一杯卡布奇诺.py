import random

menu=["Latte","Cappuccino","Iced Americano"]

print("Menu:",menu)
name=input("Please input your name:")
drink=random.choice(menu)

print("Hello,{}!\nEnjoy your {}!\n".format(name,drink))