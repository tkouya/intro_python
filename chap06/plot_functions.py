# plot_functions.py: 複数のグラフを並べる
import matplotlib.pyplot as plt # Matplotlib
import numpy as np # NumPy

# x区間の分割数を指定
n = 100

# Figureオブジェクト(fig)と
# その上にAxesオブジェクト(ax, ax2)を
# 1行2列に生成し，サイズを10x5とする
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# 三角関数のグラフを描く
# xの範囲[a, b]を指定
a = 0
b = 4 * np.pi
x_h = (b - a) / n # 小区間幅
x = [ a + i * x_h for i in range(n + 1)]

# xごとにyの値を計算
y_sin = np.sin(x)
y_cos = np.cos(x)
#y_tan = np.tan(x)

# 三角関数グラフを描画
ax.plot(x, y_sin, label='sin(x)')
ax.plot(x, y_cos, label='cos(x)')
#ax.plot(x, y_tan, label='tan(x)')
ax.set_title('y = sin(x), cos(x)')
#ax.set_title('y = sin(x), cos(x), tan(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ybound(lower=-3, upper=3)
ax.legend()
ax.grid() 

# 指数関数を対数関数をfig上に描画
# xの配列を生成し，exp(x)とlog(x)を計算
a = -3
b = 3
x_h = (b - a) / n # 小区間幅
x = [ a + i * x_h for i in range(n + 1)]
y_exp = np.exp(x)
y_log = np.log(x) # x < の時はNaNを含む

# 折れ線グラフをax2上に描画
ax2.plot(x, y_exp, label='exp(x)')
ax2.plot(x, y_log, label='log(x)')
ax2.set_title('y = exp(x), log(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_ybound(lower=-3, upper=4)
ax2.legend()
ax2.grid()

# グラフを表示
plt.show()
