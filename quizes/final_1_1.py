a = 0
b = 0
num = int(input("Enter a natural number: "))
for i in range(1, num +1):
    a = i ** 3
    b = b + a
print(b)