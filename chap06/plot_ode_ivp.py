# plot_ode_ivp.py: 常微分方程式の初期値問題と解プロット
import numpy as np
import scipy.integrate as scint  # ODEソルバー
import matplotlib.pyplot as plt  # グラフ描画

# 陽的形式の右辺
# y' = func(t, y) = y
def func(t, y):
	return y

# 初期値
# y(0) = 1
y0 = [1.0]

# t = [0, 1]
t_interval = [0.0, 1.0]
print(t_interval)

# 常微分方程式を解く
ret = scint.solve_ivp(func, t_interval, y0)  # 評価点tが可変になる
ret_fix = scint.solve_ivp(
	func, t_interval, y0,
	t_eval=np.linspace(t_interval[0], t_interval[1], 10)
)  # 評価点tが固定化される

# 結果を表示
print(ret)

# yを表示
print(ret.y)

# t-yグラフを描画
# グラフ初期化
figure, axis = plt.subplots()

# 値をセット
axis.plot(ret.t, ret.y[0, :], label='Automatic')
axis.plot(ret_fix.t, ret_fix.y[0, :], label='t_eval')

# x軸，y軸，グラフタイトルをセット
axis.set(xlabel='t', ylabel='y', title='y\' = y')

# グリッドを描画
axis.grid()

# 凡例
axis.legend()

# グラフ保存ファイル名
figure.savefig('ode.png')

# グラフを画面に描画
plt.show()

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# All rights reserved.
# -------------------------------------
