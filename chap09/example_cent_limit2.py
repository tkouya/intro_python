# example_cent_limit.py: 中心極限定理の事例
# 標本平均がx_bar以上になる確率を導出する
import numpy as np # NumPy
import scipy.stats as scstats # SciPy.stats

# 母集団の平均muと標準偏差sigmaを入力
str_mu = input('母集団の平均 = ? > ')
str_sigma = input('母集団の標準偏差 = ? > ')
mu = float(str_mu)
sigma = float(str_sigma)

# 標本平均
#str_num_x = input('標本数 = ? > ')
#num_x = float(str_num_x)
str_x_bar = input('標本の平均 = ? > ')
x_bar = float(str_x_bar)
for num_x in range(2, 1000):
    # xごとにyの値を計算: SciPy.stats.normクラスを使用
    norm_dist = scstats.norm(loc=mu, scale=sigma/np.sqrt(num_x))
    p_x_bar0 = 1.0 - norm_dist.cdf(x_bar) # 累積分布関数
    p_x_bar1 = norm_dist.sf(x_bar) # 1 - cdf(x)

    #print('p_x_bar0 = ', p_x_bar0)
    #print('p_x_bar1 = ', p_x_bar1)
    print(num_x, ' -> ', p_x_bar0, p_x_bar1)
    if p_x_bar1 <= 0.05: # 0.05以下になったらループストップ
        break # ループを終了

    # norm_distを消去
    del norm_dist

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
