# Set the maximum value we don't want to exceed
threshold = 100

# This will store the running product
product = 1

# This holds the current multiplied value
currentnumber = 1

# Keep multiplying until the value goes over the threshold
while currentnumber <= threshold:
    # Multiply the current number by the product
    currentnumber *= product

    # Increase the product for the next loop
    product += 1

# Print the final value after exceeding the threshold
print("The final product is ", currentnumber)

# Subtract 1 because product was increased after the last multiplication
print("Integer that caused the current number to exceed the threshold ", product - 1)
