from random import random

# Generate 20 random values between 0 and 1
values = [random() for i in range(20)]

# Generate a random comparison value
x = random()

# Sort the list of values
values.sort()

# Store indices where values are >= x
values_greater_than_x = []

# Check each value in the sorted list
for y in range(len(values)):
    if x <= values[y]:
        values_greater_than_x.append(y)

print("Sorted Values is ", values)
print("x = ", x)

# Print the first index where value is >= x, if it exists
if len(values_greater_than_x) > 0:
    print("The first index of x is,", values_greater_than_x[0])
else:
    print("No values greater than or equal to x")
