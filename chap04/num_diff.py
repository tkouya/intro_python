# num_diff.py: 数値微分
import numpy as np # NumPy

# 元の関数
def func(x):
    return np.exp(np.cos(x)) - x ** 3

# 真の導関数
def true_dfunc(x):
    return -np.exp(np.cos(x)) * np.sin(x) - 3 * x ** 2

# 前進差分商: (f(x + h) - f(x)) / h
def forward_diff(x, h, f):
    return (f(x + h) - f(x)) / h

# 中心差分商: (f(x + h) - f(x - h)) / 2h
def central_diff(x, h, f):
    return (f(x + h) - f(x - h)) / (2.0 * h)

# 後退差分商: (f(x) - f(x - h)) / h
def backward_diff(x, h, f):
    return (f(x) - f(x - h)) / h

# x = [-5, 5]
x = np.linspace(-5, 5, 4)
h = 10.0**(-5)

# 前進差分商，中心差分商，後退差分商
fdiff = forward_diff(x, h, func)
cdiff = central_diff(x, h, func)
bdiff = backward_diff(x, h, func)

# 相対誤差チェック
reldiff = np.abs((fdiff - true_dfunc(x)) / true_dfunc(x))
print('Forward diff relerr = ', reldiff)
reldiff = np.abs((cdiff - true_dfunc(x)) / true_dfunc(x))
print('Central diff relerr = ', reldiff)
reldiff = np.abs((bdiff - true_dfunc(x)) / true_dfunc(x))
print('Backword diff relerr= ', reldiff)

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------