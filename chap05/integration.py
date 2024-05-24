# integration.py: 数値積分による定積分+問題12.4
import numpy as np
import scipy.integrate as scint  # 積分パッケージ

# 被積分関数
def func1(x):
    return x * np.exp(np.sin(x ** 2))

# 定積分
a, b = 2, 3
ret = scint.quad(func1, a, b)

print('integral[', a, ', ', b, '] : ', ret[0])
print('ret = ', ret)
print('aE(ans)              = ', ret[1])
print('rE(ans)              = ', np.abs(ret[1] / ret[0]))
