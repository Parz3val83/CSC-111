# solution 2 part C
a = 2
for b in range(1, 23, 2):
    if a > 30:
        break
    else:
        if a != 18:
            print(a, end=' ')
    a += b
