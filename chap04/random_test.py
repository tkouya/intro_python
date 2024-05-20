# random_test.py: 乱数と統計関数
import numpy as np # NumPy

# 乱数seedの指定
rng = np.random.default_rng(seed=20240405)

# 乱数列生成
rand_vec = rng.random(3)
print('rand_vec, type(rand_vec) = ', rand_vec, type(rand_vec))
# 平均，分散，標準偏差
print('ave, var, std = %7.3g, %7.3g, %7.3g' % (np.average(rand_vec), np.var(rand_vec), np.std(rand_vec)))

# 乱数行列生成
rand_mat = rng.random((3, 3))
print('rand_mat = \n', rand_mat)
print('ave, var, std = %7.3g, %7.3g, %7.3g' % (np.average(rand_mat), np.var(rand_mat), np.std(rand_mat)))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
