# solution 5
for i in range(10, 61, 10):
    print(i, end='   ')
    for l in range(20, 61, 10):
        if l > i:
            print(l, end='   ')
        else:
            continue
    print('\n')