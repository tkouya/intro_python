# quadratic_eq2.py: 2次方程式を解く(関数呼び出し版)
#import math  # sqrt関数
import mytool # quad_eq関数

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = float(a), float(b), float(c)
print(f'  {a:25.17g} * x^2')
print(f'+ {b:25.17g} * x')
print(f'+ {c:25.17g} = 0')

# 2次方程式の解
mytool.quad_eq(a, b, c)

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
