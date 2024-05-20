# vector_matrix_function.py: ベクトル・行列を引数とする関数
import numpy as np # NumPy

# ベクトルvと行列A
vec_v = np.array([-3, -2, -1])
mat_a = np.array([
    [-1, -2, -3],
    [-2, -3, -4],
    [-3, -4, -5]
])

# 要素ごとの絶対値を求める。
print('|vec_v| = ', np.abs(vec_v))
print('|mat_a| = \n', np.abs(mat_a))

# 要素を引数とするcosineの値を求める。
print('cos(vec_v) = ', np.cos(vec_v))
print('cos(mat_a) = \n', np.cos(mat_a))
