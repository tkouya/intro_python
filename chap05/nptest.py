# nptest.py: NumPyの実行例
import numpy as np # NumPyの読み込み

# x = -3
# tan(x^3 + pi)
print('x = ', x, '-> tan(x**3 + pi) = ', np.tan(x**3 + np.pi))

# x = i
# x^x
print('x = ', x, ' -> x^x = ', x**x)

# x = [ -3i]  A = [-2  0]
#     [2+5i],     [4  5i]
# A * x
x = np.array([-3j, 2 + 5j])
A = np.array([
    [-2, 0],
    [4, -5j]
])
print('x = ', x)
print('A = ', A)
print('Ax = ', A.dot(x))
print('AX = ', A @ x)
