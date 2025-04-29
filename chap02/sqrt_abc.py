# sqrt_abc.py: 入力値の平方根とその二乗を計算
str_a = input('a =? ')
str_b = input('b =? ')
str_c = input('c =? ')

# a, b, cをfloat型に変換
a, b, c = float(str_a), float(str_b), float(str_c)

# 平方根を計算
sqrt_a, sqrt_b, sqrt_c = a**(1/2), b**(1/2), c**(1/2)

# 平方根の2乗を計算
sqrt_a2, sqrt_b2, sqrt_c2 = sqrt_a**2, sqrt_b**2, sqrt_c**2

# 結果を出力
print( '       元の数,     平方根,   平方根の2乗')
print(f'a, {a:10.3g}, {sqrt_a:10.3g}, {sqrt_a**2:13.3g}')
print(f'b, {b:10.3g}, {sqrt_b:10.3g}, {sqrt_b**2:13.3g}')
print(f'c, {c:10.3g}, {sqrt_c:10.3g}, {sqrt_c**2:13.3g}')

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
