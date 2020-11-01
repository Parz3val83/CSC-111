my_list = [6, 5, 1, -3, 10, 0, 4]
for i in range(len(my_list)):
    if my_list[i] < 3:
        my_list[i] = my_list[i] + 2
    else:
        my_list[i] = my_list[i] - 3
print(my_list)

for i in my_list[::-1]:
    if my_list.index(i) % 2 == 0:
        print(i, end=' ')