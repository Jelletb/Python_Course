import random


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'


def buildItems():
    return [Item(n, v, w) for n, v, w in (('clock', 175, 10),
                                          ('painting', 90, 9),
                                          ('radio', 20, 4),
                                          ('vase', 50, 2),
                                          ('book', 10, 1),
                                          ('computer', 200, 20))]


def buildRandomItems(n):
    return [Item(str(i), 10 * random.randint(1, 10), random.randint(1, 10))
            for i in range(n)]


# generate all combinations of N items
def power_set(items):
    n = len(items)
    # enumerate the 2**n possible combinations
    for i in range(2**n):
        combo = []
        for j in range(n):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yield_all_combos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    n = len(items)
    for i in range(3**n):
        bag1 = list()
        bag2 = list()
        for j in range(n):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)



if __name__ == '__main__':
    # items = ['stick', 'laptop', 'cup']
    # # items = ['stick']
    # # items = ['stick', 'laptop']
    # generator = power_set(items)
    # generator2 = yield_all_combos(items)
    #

    items = buildItems()
    combos = yield_all_combos(items)

    # items = buildRandomItems(3)
    # combos = yield_all_combos(items)

    for i, item in enumerate(combos):
        print(i, item)