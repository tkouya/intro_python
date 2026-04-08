# plot_num_diff.py: 数値微分と相対誤差の描画
import numpy as np # NumPy
import matplotlib.pyplot as plt # Matplotlib

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
x = np.linspace(-5, 5, 100)
h = 10.0**(-5)

# 前進差分商，中心差分商，後退差分商
fdiff = forward_diff(x, h, func)
cdiff = central_diff(x, h, func)
bdiff = backward_diff(x, h, func)

# 相対誤差チェック
reldiff_f = np.abs((fdiff - true_dfunc(x)) / true_dfunc(x))
print('Forward diff relerr = ', reldiff_f)
reldiff_c = np.abs((cdiff - true_dfunc(x)) / true_dfunc(x))
print('Central diff relerr = ', reldiff_c)
reldiff_b = np.abs((bdiff - true_dfunc(x)) / true_dfunc(x))
print('Backword diff relerr= ', reldiff_b)

# 導関数のグラフ描画
true_dfunc_y = true_dfunc(x)
print('x                   =', x)
print('True dfunc          =', true_dfunc_y)

fig, ax1 = plt.subplots()

# 関数グラフのy軸（左）を設定
ax1_color = 'red' # 赤
ax1.set_title('f\'(x) and Relerr of Numerical diff')
ax1.set_xlabel('x')
ax1.set_ylabel('f\'(x)', color=ax1_color)
ax1.plot(x, true_dfunc_y, '--', label='f\'(x)', color=ax1_color) # 赤の点線
ax1.tick_params(axis='y', labelcolor=ax1_color) # y軸に目盛を入れる

# 2番目のy軸（右）を設定
ax2 = ax1.twinx() # x軸は共通
ax2.set_ylabel('Relative Error')
ax2.set_yscale('log') # logスケールに変更
ax2.plot(x, reldiff_f, 'o', label='Forward') # 〇プロット
ax2.plot(x, reldiff_c, label='Central') 
ax2.plot(x, reldiff_b, label='Backward')
ax2.tick_params(axis='y')

# 凡例
fig.legend()

# グラフ描画
plt.show()

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# All rights reserved.
# -------------------------------------