# sin.py: サインカーブを描く
import numpy as np # NumPy

# xの範囲[a, b]を指定
a = 0
b = 4 * np.pi

# x区間の分割数を指定
n = 10

# xの配列を生成
x_h = (b - a) / n # 小区間幅
x = [ a + i * x_h for i in range(n + 1)]

# xごとにyの値を計算
y = np.sin(x)

print('x =      ', x)
print('sin(x) = ', y)

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
