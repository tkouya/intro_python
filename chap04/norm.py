# norm.py: ベクトルと行列のノルム
import numpy as np

# ベクトル
vec_a = np.array([1, 2, 3])
print('vec_a = ', vec_a)

# 行列
mat_a = np.array([[1, 2, 3], [2, 2, 3], [3, 3, 3]])
print('mat_a = \n', mat_a)

# ユークリッドノルム
print('||vec_a||_2 = ', np.linalg.norm(vec_a))
print('||mat_a||_2 = ', np.linalg.norm(mat_a))

# 1ノルム
print('||vec_a||_1 = ', np.linalg.norm(vec_a, 1))
print('||mat_a||_1 = ', np.linalg.norm(mat_a, 1))

# 無限大ノルム
print('||vec_a||_inf = ', np.linalg.norm(vec_a, np.inf))
print('||mat_a||_inf = ', np.linalg.norm(mat_a, np.inf))

# フロベニウスノルム（行列のみ）
print('||mat_a||_F = ', np.linalg.norm(mat_a, 'fro'))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
