# p06_kadai_a.py: 第６回目の課題解答例
import numpy as np # NumPy

# 1. x=-3, tan(x^3 + pi)
x = -3
print(f'{np.tan(x**3 + np.pi):25.17e}')

# 2. i^i
x = 1j
print(f'{x**x:25.17e}')

# 3. b := Ax
x = np.array([-3 * 1j, 2 + 5j])
a = np.array([
    [-2, 0],
    [4, 5j]
])
print('x = ', x)
print('A = \n', a)
b = a @ x
print('b = ', b)

