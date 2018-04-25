def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def smart_fib(n, memo={}):
    if n == 1 or n == 0:
        return 1
    else:
        try:
            return memo[n]
        except KeyError:
            memo[n] = smart_fib(n - 1) + smart_fib(n - 2)
            return memo[n]



if __name__ == '__main__':
    # for i in range(0, 3):
    #     print('Fib({}) = '.format(i) + str(fib(i)))

    for i in range(0, 120):
        print('Fib({}) = '.format(i) + str(smart_fib(i)))







