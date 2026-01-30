

def power_function(x, y):
    x**y

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []

for x in pairs:
    if x[1] < 0:
        continue
    results.append(x)

print(results)