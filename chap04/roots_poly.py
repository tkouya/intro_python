# roots_poly.py : 代数方程式を解く
import numpy as np # NumPy
import numpy.polynomial.polynomial as npppoly # Polynomialモジュール

# 次数
max_deg = 20

# 真の解 : true_roots = [n, n-1, ..., 1]
true_roots = np.array(range(max_deg, 0, -1))
print('true_roots = ', true_roots)

# 多項式p(x) = (x - n) * ... * (x - 1) の係数を生成
poly_coef = npppoly.polyfromroots(true_roots)
print('polynomial = ', poly_coef)

# 代数方程式の解(根)を導出
approx_roots = npppoly.polyroots(poly_coef)
approx_roots.sort() # 並び替え
true_roots.sort()   # 並び替え
print('approx_roots = ', approx_roots)

# 相対誤差の計算と表示
relerr_approx_roots = np.abs((approx_roots - true_roots) / true_roots)
print('relerr       = ', relerr_approx_roots)

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
