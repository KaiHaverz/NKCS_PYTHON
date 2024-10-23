num=int(input("Enter a number: "))

def isPrime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    else:
        for i in range(2,(int(num**1/2)+1) ):
            if(num%i==0):
                return False
        return True

if(isPrime(num)):
    print("Yes")
else:
    print("No")


