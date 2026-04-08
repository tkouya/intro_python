# np_calc_vec.py: リストを引数とする関数計算
import numpy as np # NumPy

# [-π/4, π/4]をn分割
n = 5 # 分割数
a, b = -np.pi / 4.0, np.pi / 4.0 # 端点
h = (b - a) / n # 区間幅

# x = [a, a + h, ..., a * (n - 1)h = b - h, a * nh = b]
xlist = np.linspace(a, b, n) #  [a + h * i for i in range(n + 1)]
print('x = ', xlist)

# tan_list = tan(x), atan_list = atan(x)
tan_list, atan_list = np.tan(xlist), np.arctan(xlist)
print(' tan(x) = ', tan_list)
print('atan(x) = ', atan_list)

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
