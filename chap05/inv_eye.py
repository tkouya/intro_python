# inv_eys.py: 単位行列と逆行列
import numpy as np

# 単位行列 I
print('Unit matrix: \n', np.eye(3)) # 正方行列
print('Unit matrix: \n', np.eye(3, 3)) # 行数と列数の指定
print('Unit matrix: \n', np.diag([1, 1, 1])) # 対角行列

# 逆行列

# 元の行列
mat_a = np.array([
    [3, 4, 0],
    [4, 3, 4],
    [3, 4, 3]
])

print('A = \n', mat_a)


# 逆行列は存在するか?
# det(A) != 0 ?
print('det(A) = ', np.linalg.det(mat_a))
# rank(A) == n ?
print('rank(A) = ', np.linalg.matrix_rank(mat_a))

inv_mat_a = np.linalg.inv(mat_a)
print('A^(-1) = \n', inv_mat_a)

# 行列 * 逆行列
print('A * A^(-1) = \n', mat_a @ inv_mat_a)
print('A^(-1) * A = \n', inv_mat_a @ mat_a)

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
