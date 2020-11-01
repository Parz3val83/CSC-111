def f(num):
    a = 0
    b = 8
    for i in range(num):
        a = (2 * b) + 14
        b = a
    return b

print(f(5))