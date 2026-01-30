from random import random
values = [random() for i in range(20)]
x = random()
values.sort()
values_greater_than_x = []

for y in range(len(values)):
    if x <= values[y]:
        values_greater_than_x.append(y)


print("Sorted Values is ", values)
print("x = ",x)

if len(values_greater_than_x) > 0:
    print("The first index of x is,", values_greater_than_x[0])
else:
    print("No values greater than or equal to x")
