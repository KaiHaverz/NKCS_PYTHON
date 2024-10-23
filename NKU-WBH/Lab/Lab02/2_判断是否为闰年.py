year=int(input("请输入年份:"))

def isRN(year):
    if((year%4==0 and year%100!=0) or (year%400==0)):
        return True
    else:
        return False

if (isRN(year)==True):
    print("%d是闰年" %year)
else:
    print("%d不是闰年" %year)