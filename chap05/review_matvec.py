# review_matvec.py: ベクトル演算，行列演算
import numpy as np # NumPy

# ベクトルと行列の定義
vec_x = np.array([1, 2])
vec_y = np.array([-2, -3])
mat_a = np.array([
    [4, 3],
    [5, 4]
])
mat_b = np.array([
    [-2, -3],
    [-3, -4]
])
print('x, y = ', vec_x, vec_y)
print('A = \n', mat_a)
print('B = \n', mat_b)

# ベクトル，行列演算
vec_z = -4 * vec_x - 7 * vec_y
mat_c = -4 * mat_a - 7 * mat_b
print('z = -4 * x - 7 * y = ', vec_z)
print('C = -4 * A - 7 * B = \n', mat_c)

# 行列・ベクトル積
vec_b = mat_a @ vec_x
print('b = A * x = ', vec_b)

# ベクトルノルム
print('||x||_2 = ', np.linalg.norm(vec_x))
print('||y||_2 = ', np.linalg.norm(vec_y, ))
print('||x-y||_2 = ', np.linalg.norm(vec_x - vec_y))

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
