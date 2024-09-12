def hanoi(n,source,target,aux):
    if n==1:
        print(f'Move dish 1 from {source} to {target}')
        return
    hanoi(n-1,source,target,aux)
    print(f'Move {n} from {source} to {target}')
    hanoi(n-1,aux,source,target)


count=input("Please enter the number of disks:")
hanoi(int(count),"A","B","C")