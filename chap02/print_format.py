# print_format.py: 書式付き出力

str_a = input('a = ')
str_b = input('b = ')

# 文字列の表示
print('str_a, str_b = ', str_a, str_b) # 書式指定なし
print('str_a, str_b = %10s, %s' % (str_a, str_b)) # 書式化演算子%
print('str_a, str_b = {:10s}, {}'.format(str_a, str_b)) # formatメソッド
print(f'str_a, str_b = {str_a:10s}, {str_b:s}') # f文字列

# 整数の表示
int_a = int(str_a) # 文字列→整数
int_b = int(str_b)
print('int_a, int_b = ', int_a, int_b) # 書式指定なし
print('int_a, int_b = %10d, %d' % (int_a, int_b)) # 書式化演算子%
print('int_a, int_b = {:10d}, {:d}'.format(int_a, int_b)) # formatメソッド
print(f'int_a, int_b = {int_a:10d}, {int_b:d}') # f文字列, 10進表示
print(f'int_a, int_b = {int_a:b}, {int_b:b}') # f文字列, 2進表示
print(f'int_a, int_b = {int_a:o}, {int_b:o}') # f文字列, 8進表示
print(f'int_a, int_b = {int_a:#o}, {int_b:#o}') # f文字列, 8進表示, 0o-prefix
print(f'int_a, int_b = {int_a:x}, {int_b:x}') # f文字列, 16進表示
print(f'int_a, int_b = {int_a:#x}, {int_b:#x}') # f文字列, 16進表示, 0x-prefix

# 浮動小数点数(実数)の表示
float_a = float(str_a)
float_b = float(str_b)
print('float_a, float_b = ', float_a, float_b) # 書式指定なし
print('float_a, float_b = %15g, %g' % (float_a, float_b)) # 書式化演算子%
print('float_a, float_b = {:15g}, {:g}'.format(float_a, float_b)) # formatメソッド
print(f'float_a, float_b = {float_a:15g}, {int_b:g}') # f文字列
print(f'float_a, float_b = {float_a:15.2f}, {int_b:f}') # f文字列, 小数表示
print(f'float_a, float_b = {float_a:20.15e}, {int_b:e}') # f文字列, 指数表示

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
