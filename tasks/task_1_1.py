import math


def lgn(n):
    return math.log(n, 10)


def sqrtn(n):
    return pow(n, 0.5)


def nn(n):
    return n


def nlgn(n):
    return n * math.log(n, 10)


def pown2(n):
    return n * n


def pown3(n):
    return math.pow(n, 3)


def pow2n(n):
    return math.pow(2, n)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
