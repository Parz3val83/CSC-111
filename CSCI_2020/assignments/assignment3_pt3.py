def perform_operation(a, b, c):
    for index in range(len(a)):
        a_mult = 2 * a[index]
        b_mult = 3 * b[index]
        sum_a_b = a_mult + b_mult -5
        c.append(sum_a_b)
    return c

a = [1, 4, 2, 5]
b = [2, 3, 6, 4]
c = []
result = perform_operation(a, b, c)
print(result)