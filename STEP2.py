import numpy as np

data = np.array([10, 20, 30, 40])
print(np.mean(data))
print(np.var(data))
print(np.std(data))


# 最大値と最小値も表示する
print(np.max(data))
print(np.min(data)) 

# すべての値を2倍した新しい配列を作成する
doubled_data = data * 2     
print(doubled_data) 
