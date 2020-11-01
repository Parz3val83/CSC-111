def shift_left(a):
    for i in a:
        if a.index(i) == 0:
            a.remove(i)
            a.insert(len(a), i)
    return a 


def shift_right(a):
    for i in a:
        if a.index(i) == len(a) -1:
            a.remove(i)
            a.insert(0, i)
    return a


list1 = [6, 3, 2, 4, 7]
print(list1)
print(shift_left(list1))
print(shift_right(list1))
