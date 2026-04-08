# plot_ode_ivp_relerr.py: 常微分方程式の初期値問題と解プロット
import numpy as np # NumPy
import scipy.integrate as scint  # ODEソルバー
import matplotlib.pyplot as plt  # グラフ描画

# 陽的形式の右辺
# y' = func(t, y) = y or -ty
def func(t, y):
	# return y
	return -t * y

# 真の解
# y(t) = exp(t) or -t^2/2
def true_sol(t):
	# return np.exp(t)
	return np.exp(-t ** 2 / 2.0)

# 初期値
# y(0) = 1
y0 = [1.0]

# t = [0, 1]
t_interval = [0.0, 1.0]
print(t_interval)

# tの評価点をfix
t_val = np.linspace(t_interval[0], t_interval[1], 10)

# 常微分方程式を解く
ret = scint.solve_ivp(func, t_interval, y0)  # 評価点tが可変になる
ret_fix = scint.solve_ivp(
	func, t_interval, y0,
	t_eval=t_val
)  # 評価点tが固定化される

# 結果を表示
print(ret)

# yを表示
print(ret.y)

# 相対誤差を計算
relerr_ret_fix = np.abs(ret_fix.y[0, :] - true_sol(ret_fix.t)) / np.abs(true_sol(ret_fix.t))

# t-yグラフを描画
# グラフ初期化
figure, axis = plt.subplots()

# 値をセット
axis.plot(ret.t, ret.y[0, :], label='Automatic')
t_eval_color = 'red'
axis.plot(ret_fix.t, ret_fix.y[0, :], label='t_eval', color=t_eval_color)

# x軸，y軸，グラフタイトルをセット
axis.set(xlabel='t', ylabel='y', title='y\' = -ty') # y')

# グリッドを描画
axis.grid()

# 相対誤差用のy軸
axis2 = axis.twinx()
axis2.set_ylabel('Relative Error', color=t_eval_color)
axis2.set_yscale('log') # logスケールに変更
axis2.plot(ret_fix.t, relerr_ret_fix, '--', label='Relative Error', color=t_eval_color)

# 凡例
figure.legend()

# グラフを画面に描画
plt.show()

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# All rights reserved.
# -------------------------------------
