import pandas as pd

# Data for creating the DataFrame
columnData = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create a DataFrame from the dictionary
dataFrame = pd.DataFrame(columnData)

# Create a new column by multiplying columns A and B
dataFrame["ComputedColumn"] = dataFrame["A"] * dataFrame["B"]

print(dataFrame)
