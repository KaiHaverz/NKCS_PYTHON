from functools import reduce
def fn(x,y):
    return x*10+y
def CharToInt(s):
    return  {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

if __name__ == '__main__':
    result=reduce(fn,map(CharToInt,'13579'))
    print(result)
    print(type(result))