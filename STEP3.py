import pandas as pd

df = pd.DataFrame({
    "age": [20, 30, 40],
    "income": [300, 500, 700]
})

print(df)
print(df.describe())