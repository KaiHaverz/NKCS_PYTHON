def Hanoi(n,src,target,aux):
    if n==1:
        print(f'move {src} to {target}')
        return
    Hanoi(n-1,src,aux,target)
    print(f'move {src} to {target}')
    Hanoi(n-1,aux,target,src)



num=int(input("Enter number of rods: "))
Hanoi(num,"source","target","aux")
