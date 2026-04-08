# linear_eq.py: 連立一次方程式を解く
import numpy as np # NumPy

# 係数行列Aを定義
A = np.array([
    [2, 3],
    [3, -1]
])

# 定数ベクトルを定義
b = np.array([3, 1])

# 行列A, ベクトルbの確認
print('A = \n', A)
print('b = ', b)

# 連立一次方程式を解く
# x = A^(-1) * b
x = np.linalg.inv(A) @ b

print('x = ', x)

# 検算: Ax = b ?
print('Ax = ', A @ x)

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
