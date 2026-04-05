import matplotlib.pyplot as plt 
import pandas as pd

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "income": [300, 350, 500, 650, 800]
})

# study_time 列を追加して、他の列との相関を見る
df["study_time"] = [1, 2, 2, 3, 5]


print(df.corr())

# ageとincomeの相関をmatplotlibで可視化
plt.scatter(df["age"], df["income"])
plt.xlabel("Age")       
plt.ylabel("Income")
plt.title("Age vs Income")      
plt.show()  





