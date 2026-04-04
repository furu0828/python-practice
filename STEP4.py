import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40], 
    "income": [300, 350, 500, 650, 800]
})

plt.hist(df["age"])
plt.show()


# ageのbinsを5にしてヒストグラムを描く
plt.hist(df["age"], bins=5) 
plt.show()  

# ageとincomeの散布図を描く
plt.scatter(df["age"], df["income"])        
plt.show()  
