def hanoi(n,source,target,aux):
    if n==1:
        print(f'Move dish 1 from {source} to {target}')
        return
    hanoi(n-1,source,aux,target)
    print(f'Move dish {n} from {source} to {target}')
    hanoi(n-1,aux,target,source)


count=input("Please enter the number of disks:")
hanoi(int(count),"Source","Target","Aux")