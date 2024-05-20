# products.py: ベクトルのドット積，内積，行列・ベクトル積，行列積
import numpy as np

# ベクトル
vec_a = np.array([1, 2, 3])
vec_b = np.array([-3, -2, -1])

print('vec_a = ', vec_a)
print('vec_b = ', vec_b)

# ドット積
ip_ab = vec_a.dot(vec_b)
print('(a, b) = ', ip_ab)

# 複素ベクトル
vec_c = np.array([1 + 1j, -2 + 2j])
vec_d = np.array([-2 + 3j, -1 - 4j])
print('vec_c = ', vec_c)
print('vec_d = ', vec_d)

# ドット積と内積
dot_cd = vec_c.dot(vec_d)
ip_cd = np.conj(vec_c).dot(vec_d)
print(' c . d = ', dot_cd)
print('(c, d) = ', ip_cd)

# 行列
mat_a = np.array([[1, 2, 3], [2, 2, 3], [3, 3, 3]])
mat_b = np.array([[-3, -3, -3], [-3, -2, -2], [-3, -2, -1]])
print('mat_a = \n', mat_a)
print('mat_b = \n', mat_b)

# 行列・ベクトル積
mat_av = mat_a.dot(vec_a)
print('A * a = ', mat_av)

# 行列乗算
mat_ab = mat_a.dot(mat_b)
print('A * B = \n', mat_ab)
mat_ab_at = mat_a @ mat_b
print('A @ B = \n', mat_ab_at)
