# matmul_bench.py: 行列乗算ベンチマーク
import numpy as np # NumPy
from time import time # 時間計測

# 乱数seedの指定
rng = np.random.default_rng(seed=20240405)

# 行列サイズ入力
str_dim = input('Input dimension = ')
dim = int(str_dim)

# 乱数行列生成
mat_a = rng.random((dim, dim))
mat_b = rng.random((dim, dim))

# 行列乗算1
stime = time()
mat_c_dot = mat_a.dot(mat_b)
dot_time = time() - stime

# 行列乗算2
stime = time()
mat_c_at = mat_a @ mat_b
at_time = time() - stime

# 出力
print('||C_dot||_F = %25.17e' % np.linalg.norm(mat_c_dot, 'fro'))
print('||C_at ||_F = %25.17e' % np.linalg.norm(mat_c_at , 'fro'))
print('s(C_dot), s(C_at) = %7.3f, %7.3f' % (dot_time, at_time))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
