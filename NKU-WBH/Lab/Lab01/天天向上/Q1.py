grade=1.0
everyday_effort = float(input("请输入你每天的进步量:")) #将字符型变量转换为浮点型,便于之后的计算
def func(everyday_effort):
    global grade # 声明grade为全局变量
    grade *= ((1+everyday_effort)**365)
    return grade

# 输出为 %f,不是%d,控制有效数字长度(小数位数)
print("你每天努力进步%.3f,一年后你的成绩是%.5f" % (everyday_effort,func(everyday_effort)) )
