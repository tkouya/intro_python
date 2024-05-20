# first_matrix.py: 最初の行列演算
import numpy as np # NumPy

# 行列
mat_a = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
])
mat_b = np.array([
    [-3, -2, -1],
    [-2, -1,  0],
    [-1,  0,  1]
])

print('mat_a = \n', mat_a)
print('mat_b = \n', mat_b)

# 行列演算ができる
mat_c = 3 * mat_a + mat_b
print('mat_c = \n', mat_c)
