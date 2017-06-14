def bit_sum(a, b):
    c = list()
    in_memory = 0
    for i in range(0, len(a)):
        ind = len(a) - (i + 1)
        row_c = a[ind] + b[ind] + in_memory
        c.insert(0, row_c % 2)
        in_memory = 0 if row_c < 2 else 1
    c.insert(0, in_memory)
    return c
