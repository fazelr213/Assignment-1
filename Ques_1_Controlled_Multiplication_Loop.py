threshold = 100
product = 1
currentnumber = 1


while currentnumber <= threshold:
    currentnumber *= product
    product += 1


print("The final product is ", currentnumber)
print("Integer That caused the current number to exceed the threshold ", product - 1)