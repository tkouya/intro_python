# plot_cosine.py: コサインカーブを描く
import matplotlib.pyplot as plt # Matplotlib
import numpy as np # NumPy

# xの範囲[a, b]を指定
a = 0
b = 4 * np.pi

# x区間の分割数を指定
n = 150 # 画面解像度と関数の変化率による

# xの配列を生成
x_h = (b - a) / n # 小区間幅
x = [ a + i * x_h for i in range(n + 1)]

# xごとにyの値を計算
# y = np.sin(x)
y = np.cos(x)

# 2次元グラフを描画
# (1) Figureオブジェクト(fig)と
# その上にAxesオブジェクト(ax)を生成
fig, ax = plt.subplots()

# (2) 折れ線グラフをax上に描画
ax.plot(x, y)

# (3) グラフタイトル，x軸タイトル，y軸タイトルを指定
ax.set_title('y = cos(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')

# (4) グリッドを描画
ax.grid() 

# (5) グラフを表示
plt.show()

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
