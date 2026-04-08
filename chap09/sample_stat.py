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

x2_stat = [
    np.average(x2), # 平均値
    np.var(x2),     # 分散
    np.std(x2),     # 標準偏差
    np.max(x2),     # 最大値
    np.min(x2),     # 最小値
    np.median(x2)   # 中央値
]
# (1) np.float64がくっつく
# print('x2_stat = ', x2_stat)
# (2) np.float64を消したい場合
print('x2_stat = ', end='')
for val in x2_stat:
    print(f'{val:g}', end=' ')
print() # 最後は改行

# 分散 == 標準偏差^2
print('x1: var == std**2: ', x1_stat[1], x1_stat[2]**2)
print('x2: var == std**2: ', x2_stat[1], x2_stat[2]**2)

# 中央値 = sort()
x1.sort() # 昇順で並べ替え
mid_i = int(len(x1) / 2) # len(x1)=5-> mid_i 5/2=2 -> mid_i = 2
if len(x1) % 2 != 0:
    print('x1.sort: ', x1, ' -> ', x1_stat[5], x1[mid_i])
else:
    median = (sorted(x1)[mid_i - 1] + sorted(x1)[mid_i]) / 2
    print('x1.sort: ', x1, ' -> ', x1_stat[5], median)

# 中央値 = sort()
x2.sort() # 昇順で並べ替え
mid_i = int(len(x2) / 2) # len(x2)=5-> mid_i 5/2=2 -> mid_i = 2
if len(x2) % 2 != 0:
    print('x2.sort: ', x2, ' -> ', x2_stat[5], x2[mid_i])
else:
    median = (x2[mid_i - 1] + x2[mid_i]) / 2
    print('x2.sort: ', x2, ' -> ', x2_stat[5], median)

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
