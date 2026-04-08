# np_calc.py: NumPyの初等関数機能
import numpy as np  # NumPy

a = -3.0
z = -1.0 + 2.0j

print('a = ', a)
print('z = ', z)

# 平方根: NumPy
print('np.sqrt(a) = ', np.sqrt(a))
print('np.sqrt(z) = ', np.sqrt(z))

# べき乗: NumPy
c = np.sqrt(a)
w = np.sqrt(z)
print('(np.sqrt(a))^2 = ', c ** 2)
print('(np.sqrt(z))^2 = ', w ** 2)

# 指数関数，三角関数，対数関数: NumPy
print('np.exp(a)   = ', np.exp(a))
print('np.sin(a)   = ', np.sin(a))
print('np.log(a)   = ', np.log(a))
print('np.log10(a) = ', np.log10(a))
print('np.exp(z)   = ', np.exp(z))
print('np.sin(z)   = ', np.sin(z))
print('np.log(z)   = ', np.log(z))
print('np.log10(z) = ', np.log10(z))

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
