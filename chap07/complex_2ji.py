# complex_2ji.py: Gauss平面上に2次関数を描画
import numpy as np
import matplotlib.pyplot as plt

# 関数の定義
def f(x):
    return x**2 + x + 1

# 実数部と虚数部の範囲を設定
real = np.linspace(-2, 2, 400)
imag = np.linspace(-2, 2, 400)

# 格子点を作成
X, Y = np.meshgrid(real, imag)
Z = X + 1j * Y

# 関数を評価
W = f(Z)

# プロット
plt.figure(figsize=(10, 8))

# 実数部のプロット
plt.subplot(2, 1, 1)
plt.contourf(X, Y, W.real, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Real part of f(x) = x^2 + x + 1')
plt.xlabel('Real part of x')
plt.ylabel('Imaginary part of x')

# 虚数部のプロット
plt.subplot(2, 1, 2)
plt.contourf(X, Y, W.imag, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Imaginary part of f(x) = x^2 + x + 1')
plt.xlabel('Real part of x')
plt.ylabel('Imaginary part of x')

plt.tight_layout()
plt.show()
