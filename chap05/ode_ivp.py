# ode_ivp.py: 常微分方程式の初期値問題
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

# 常微分方程式を解く(1)
ret = scint.solve_ivp(func, t_interval, y0)  # 評価点tが可変になる
ret_fix = scint.solve_ivp(
	func, t_interval, y0,
	t_eval=np.linspace(t_interval[0], t_interval[1], 10)
)  # 評価点tが固定化される

# 結果を表示
print(ret)

# yを表示
print(ret.y)