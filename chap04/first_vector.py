# first_vector.py: 最初のベクトル演算
import numpy as np # NumPy

# ベクトル
vec_a = np.array([1, 2, 3])
vec_b = np.array([-3, -2, -1])

print('vec_a = ', vec_a)
print('vec_b = ', vec_b)

# ベクトル演算ができる
vec_c = 3 * vec_a + vec_b
print('vec_c = ', vec_c)