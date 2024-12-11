# 加入钩子
def flatten_list(nested):
    if isinstance(nested, list):
        for sublist in nested:
            print("ccc")
            for item in flatten_list(sublist):
                print("ppp")
                yield item
                print("yyy")


    else:
        print("uuu")
        yield nested
        print("xxx")

def main():
    raw_list=["a",["b","c",["d"]]]
    g=flatten_list(raw_list)
    print(next(g),"***")
    print(next(g),"---")

main()