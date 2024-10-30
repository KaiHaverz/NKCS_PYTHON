def f(x):
    return x*x

if __name__ == '__main__':
    r = map(f,[1,2,3,4,5,6,7,8,9])
    s=map(str,[1,2,3,4,5,6,7,8,9])
    print(type(r))
    print(type(s))
    print(list(r))
    print(list(s))