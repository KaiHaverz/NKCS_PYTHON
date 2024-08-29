import random

meet = ["鱼香肉丝","回锅肉","酸菜鱼","宫保鸡丁"]
vegetable = ["藤藤菜","四季豆","拍黄瓜","番茄炒蛋"]
desert = ["红糖糍粑","凉糕","冰汤圆"]
          
name = input("Hello, Welcome to SDS Resteraunt! Please input your name: ")

randomMeet = random.choice(meet)
randomVegetable = random.choice(vegetable)
randomDesert = random.choice(desert)

print("Hello, ",name,"! Today your dinner dish is ",randomMeet,randomVegetable,randomDesert,"\nEnjoy the meal!")