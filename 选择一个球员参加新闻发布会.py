import random
players = ["Tim","Romulo", "Timo", "Felipe", "Ganchao"]
print("Players",players)

name = input("input your name please: ")
attendPlayer = random.choice(players)
print("Hello,",name,"! Today ",attendPlayer," will attend this meeting with you.\nGood luck for tommorow's game!")