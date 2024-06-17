# eig.py: 正方行列の固有値・固有ベクトル
import numpy as np # NumPy
import scipy.linalg as sclinalg # SciPy.linalg

# 乱数seedの指定
rng = np.random.default_rng(seed=20240521)

# 正方行列の次数
input_str = input('Input size of square matrix > ')
n = int(input_str)

# 乱数行列生成
mat_a = rng.random((n, n))
print('mat_a = \n', mat_a)

# 全ての固有値
eigen_values = sclinalg.eig(mat_a)

# 固有値，(右)固有ベクトル
eigen_values, Vr = sclinalg.eig(mat_a, right=True)
print('Eigenvalues = ', eigen_values)
print('Right eigenvectors = ', Vr)

# 固有値，左固有ベクトル，(右)固有ベクトル
eigen_values, Vl, Vr = sclinalg.eig(mat_a, left=True, right=True)
print('Eigenvalues = ', eigen_values)
print('Left eigenvectors = \n', Vl)
print('Right eigenvectors = \n', Vr)

print('index ||(A - eig * I) Vr || / ||Vr||  ||(A - eig * I) Vl|| / ||Vl||')
for index in range(n):
    # A * Vr == Labmda * Vr ?
    print(f'{index:5d} {np.linalg.norm((mat_a - eigen_values[index] * np.eye(n)) @ Vr[:, index]) / np.linalg.norm(Vr[:, index]):30.17e} {np.linalg.norm((mat_a.T - eigen_values[index].conj() * np.eye(n)) @ Vl[:, index]) / np.linalg.norm(Vl[:, index]):30.17e}')

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# All rights reserved.
# -------------------------------------
