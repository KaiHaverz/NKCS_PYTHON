def f_to_c(f):
    c=(f-32)/1.8
    return round(c,2)

f=float(input("请输入华氏度:"))
c=f_to_c(f)
print(f"摄氏度为:{c}",)