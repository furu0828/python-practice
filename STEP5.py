import pandas as pd

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "income": [300, 350, 500, 650, 800]
})

print(df.corr())