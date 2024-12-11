def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

fah=float(input("请输入华氏度:"))

print("相当于%.2f摄氏度" % fahrenheit_to_celsius(fah))