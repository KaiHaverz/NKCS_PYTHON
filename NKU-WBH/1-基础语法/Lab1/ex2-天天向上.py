# Q1
print("Q1:")
print("每天进步0.1%，一年之后的水平是:",1.001**365)
print("每天退步0.1%，一年之后的水平是:",0.999**365)
print("每天进步0.5%，一年之后的水平是:",1.005**365)
print("每天退步0.1%，一年之后的水平是:",0.995**365)
print("每天进步1%，一年之后的水平是:",1.01**365)
print("每天退步1%，一年之后的水平是:",0.99**365)

print("\n-------------------------------\nQ2:")

level=1.0
another_day=1
work_day=5
rest_day=2
week=52

for i in range(1,53):
    level=level*(1.01**5)
    level=level*(0.99**2)

final_level=level*1.01
print("一年后你的水平是:",final_level)

print("\n-------------------------------\nQ3:")


import math

progress_rate=math.pow( ((1.01**365)/(0.99**104)) ,1/261)

print("B君需要在工作日每天进步",(progress_rate-1)*100,"%")

