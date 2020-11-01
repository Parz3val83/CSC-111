def question_3(a, b):
    if len(a) % 2 == 1 and len(b) % 2 != 0:
        print('List A:', a, 'List B:', b)
        temp_a0 = a[0]
        temp_a3 = a[3]
        temp_b0 = b[0]
        temp_b3 = b[3]
        a[0] = temp_b0
        b[0] = temp_a0
        a[3] = temp_b3
        b[3] = temp_a3
        print('list A:', a, 'list B;', b)


A = [2, 4, 5, 8, 9]

B = [13, 14, 16, 21, 25]


question_3(A, B)
