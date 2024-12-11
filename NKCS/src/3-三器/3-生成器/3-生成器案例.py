def flatten_list(nested):
    if isinstance(nested, list):
        for sublist in nested:
            for item in flatten_list(sublist):
                yield item

    else:
        yield nested


def main():
    raw_list=["a",["b","c",["d"]]]
    g=flatten_list(raw_list)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print("flatten_list is: ",list(flatten_list(raw_list)))


main()