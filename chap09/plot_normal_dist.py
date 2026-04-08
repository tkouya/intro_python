# plot_normal_dist.py: 正規分布のグラフを描画する
import matplotlib.pyplot as plt # Matplotlib
import numpy as np # NumPy
import scipy.stats as scstats # SciPy.stats

# 平均muと標準偏差sigmaを入力
str_mu = input('mu = ? > ')
str_sigma = input('sigma = ? > ')
mu = float(str_mu)
sigma = float(str_sigma)

# xの範囲[a, b]を指定
a = mu + sigma * 5
b = mu - sigma * 5

# x区間の分割数を指定
n = 50 # 画面解像度と関数の変化率による

# xの配列を生成
x_h = (b - a) / n # 小区間幅
x = [ a + i * x_h for i in range(n + 1)]

# xごとにyの値を計算: NumPy関数を使用
y = [(1.0 / (np.sqrt(np.pi * 2) * sigma)) * np.exp(-(x[i] - mu)**2 / (2 * sigma**2)) for i in range(n + 1)]

# xごとにyの値を計算: SciPy.stats.normクラスを使用
norm_dist = scstats.norm(loc=mu, scale=sigma)
y_stat = norm_dist.pdf(x)

# 2次元グラフを描画
fig, ax = plt.subplots()
ax.plot(x, y, label='NumPy') # 直線
ax.plot(x, y_stat, 'o', label='SciPy.stat', color='red') # 〇でプロット
ax.set_title('N(' + str(mu) + ', ' + str(sigma**2) + ')')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid() 
ax.legend()
plt.show()

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
