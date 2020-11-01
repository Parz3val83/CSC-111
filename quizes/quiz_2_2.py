a = 4
c = 21
while c <= 34:
    if a <= 13:
        print(a, end=' ')
        a += 3
    else:
        c += 4
        print(c, end=' ')


a = 3
b = 0
print(a, end=' ')
for x in range(8):
    b = a + 4
    a = b
    if b != 23:
        print(b, end=' ')