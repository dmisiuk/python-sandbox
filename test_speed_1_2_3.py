import math


def f(n):
    return 100 * n * n


def g(n):
    return math.pow(2, n)


x = 1
while True:
    fn = f(x)
    gn = g(x)
    print('f>g = {}: f({})= {}, g({})={}, '.format(fn > gn, x, fn, x, gn))
    if fn < gn:
        print("from {} 100n^2 grow slowly than 2^n".format(x))
        break

    x = x + 1
