# create variables to store user data
num1 = float(input("Enter an number: "))
num2 = float(input("Enter another number: "))
num3 = float(input("Enter a third number: "))
num4 = float(input("Enter your final number: "))

# store total
total = num1 + num2 + num3 + num4
# find average of teh user input
average = total / 4

# determine max using using if-else
max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
if num4 > max:
    max = num4
# determine min with if-else
min = num1
if num2 < min:
    min = num2
if num3 < min:
    min = num3
if num3 < min:
    min = num4

# calculate median using total and max min
median = (total - min - max) / 2

# format and print four values
print("The minimum is,", min, ", the maximum is,", max, ".")
print("The mean is,", average, "and the median is,", median, ".")
