from timeit import timeit
import matplotlib.pyplot as plt
import numpy as n


NUMBER1 = 3


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def look_for_things(myList):
    """Looks at all elements"""
    for n in myList:
        if n == NUMBER1:
            return True
    return False

NUMBER2 = 4


def look_for_other_things(myList):
    """Looks at all pairs of elements"""
    for n in myList:
        for m in myList:
            if n - m == NUMBER2 or m - n == NUMBER2:
                return True
    return False


def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

NUMBER3 = 4


def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER3:
            return True
    return False


if __name__ == '__main__':
    test = [0]
    time = list()
    length = list()

    for i in range(1, 20):
        test = list(n.zeros(len(test)))
        test.append(3)
        # Insert function to test
        x = wrapper(look_for_all_the_things, test)
        x = timeit(x, number=10)
        time.append(x)
        length.append(len(test))

    plt.figure()
    plt.plot(length, time)
    plt.xlabel('Length MyList')
    plt.ylabel('Run time')
    plt.show()






