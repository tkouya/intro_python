# test_quad.py: 数値積分の例
import numpy as np # NumPy
from scipy.integrate import quad # SciPy.integrate

# 積分する関数を定義（例: f(x) = x^2）
def f(x):
    return x**2

# 区間[0, 1]で定積分を計算
result, error = quad(f, 0, 1)

print("積分結果:", result) # 結果を表示
print("推定誤差:", error)  # 推定誤差を表示

# 積分する関数を定義（例: f(x) = sin(1/x)）
def g(x):
    return np.sin(1 / x)

result, error = quad(g, 0, 1)

print("積分結果:", result) # 結果を表示
print("推定誤差:", error)  # 推定誤差を表示