def power_function(x, y):
    x ** y  # calculates x raised to the power y (note: no return yet)


pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []

for x in pairs:
    # Skip pairs where the exponent is negative
    if x[1] < 0:
        continue

    # Keep only pairs with non-negative exponents
    results.append(x)

print(results)
