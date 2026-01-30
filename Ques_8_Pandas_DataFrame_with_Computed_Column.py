import pandas as pd

columnData = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

dataFrame = pd.DataFrame(columnData)

dataFrame["ComputedColumn"] = dataFrame["A"] * dataFrame["B"]

print(dataFrame)
