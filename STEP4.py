import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40, 45, 50]
})

plt.hist(df["age"])
plt.show()