import pandas as pd

df = pd.DataFrame({
    "age": [20, 30, 40],
    "income": [300, 500, 700]
})

print(df)
# print(df.describe())

# score 列を追加して、テスト点数を入れる
df["score"] = [80, 90, 85]
print(df)   
