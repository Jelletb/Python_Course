# contents = (name, weight, value)

contents = [['Dirt', 4, 0],
            ['Computer', 10, 30],
            ['Fork', 5, 1],
            ['Problem Set', 0.000001, -10]]

weight_limit = 14


def metric1(item):
    return item[2] / item[1]


def metric2(item):
    return -item[1]


def metric3(item):
    return item[2]


for item in contents:
    item.append(metric3(item))  # Edit metric to suit your needs

contents_sorted = sorted(contents, key=lambda cont: cont[3], reverse=True)

print(contents_sorted)

weight = 0
value = 0
for item in contents_sorted:
    if weight + item[1] <= weight_limit:
        weight += item[1]
        value += item[2]

print('Total weight = {}'.format(str(weight)))
print('Total value = {}'.format(str(value)))


