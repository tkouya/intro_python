# sample_stat.py: 平均，分散，標準偏差の計算
import numpy as np # NumPy

# 離散データの入力
x1 = [3.0, 4.5, 2.0, 3.0, 3.4]
x2 = [-3.4, 4.0, 10.0, 4.0, -2]

x1_stat = [
    np.average(x1), # 平均値
    np.var(x1),     # 分散
    np.std(x1),     # 標準偏差
    np.max(x1),     # 最大値
    np.min(x1),     # 最小値
    np.median(x1)   # 中央値
]
# (1) np.float64がくっつく
# print('x1_stat = ', x1_stat)
# (2) np.float64を消したい場合
print('x1_stat = ', end='')
for val in x1_stat:
    print(f'{val:g}', end=' ')
print() # 最後は改行