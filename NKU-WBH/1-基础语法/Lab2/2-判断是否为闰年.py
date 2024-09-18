def is_runNian(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False


year=int(input("please enter year:"))

if is_runNian(year):
    print(f"{year} is runnian")
else:
    print(f"{year} is not runnian")