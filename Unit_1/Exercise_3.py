from timeit import timeit


NUMBER = 3


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def look_for_things(myList):
    """Looks at all elements"""
    for n in myList:
        if n == NUMBER:
            return True
    return False

if __name__ == '__main__':
    # x_list = [1, 1, 1, 1, 3]
    # x = wrapper(look_for_things, x_list)
    # x = timeit(x, number=100000)
    # y_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    # y = wrapper(look_for_things, y_list)
    # y = timeit(y, number=100000)
    #
    # dlength = len(y_list) / len(x_list)
    # dtime = y / x

    test = list()
    time = list()
    length = list()

    for i in range(1, 100):
        test.append(i)
        x = wrapper(look_for_things, test)
        x = timeit(x, number=1000)
        time.append(x)
        length.append(len(test))






