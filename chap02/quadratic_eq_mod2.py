# quadratic_eq_mod.py: 2次方程式を解く(複素解対応版)
import math  # sqrt関数

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = float(a), float(b), float(c)
print(f'  {a:25.17g} * x^2')
print(f'+ {b:25.17g} * x')
print(f'+ {c:25.17g} = 0')

# 判別式
d = b ** 2 - 4 * a * c

if d >= 0: # 実数解の場合
    print('Real solutions: \n')
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    # 出力
    print(f'x1 = {x1:25.17e}')
    print(f'x2 = {x2:25.17e}')
else: # 複素数解の場合
    print('complex solutions: \n')
    x1 = complex(-b / (2 * a), math.sqrt(-d) / (2 * a))
    x2 = complex(-b / (2 * a), -math.sqrt(-d)) / (2 * a)
    # 出力
    print(f'x1 = {x1:25.17e}')
    print(f'x2 = {x2:25.17e}')

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
