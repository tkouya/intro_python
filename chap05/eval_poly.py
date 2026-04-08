# eval_poly.py : 多項式の計算
import numpy as np # NumPy
import numpy.polynomial.polynomial as npppoly # Polynomialモジュール

# 係数を指定した公式の定義
# p(x) = 2 + 0 * x + 2 * x^2 + 4 * x^3
p_coef = np.array([2, 0, 2, 4]) # 単なるリストも可
print('p(x) = ', p_coef)

# p(3)の値の計算
print('p(3) = ', npppoly.polyval(3, p_coef))

# p(x)の導関数p'(x)とp'(3)の計算
dp_coef = npppoly.polyder(p_coef) # 係数の計算
print('p\'(x) = ', dp_coef)
print('p\'(3) = ', npppoly.polyval(3, dp_coef))

# p(x)の原始関数P(x)とP(3)の計算
ip_coef = npppoly.polyint(p_coef) # 係数の計算
print('P(x) = ', ip_coef)
print('P(3) = ', npppoly.polyval(3, ip_coef))

# p(x) = 0の解
sols = npppoly.polyroots(p_coef)
print('roots of p(x) = ', sols)

# 検算 p(x) == 0?
p_vals = npppoly.polyval(sols, p_coef)
print('p(roots) = ', p_vals)

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
