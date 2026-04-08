# input_complex.py: 複素数の入力
str_a = input('Re(c) = a =? ')
str_b = input('Im(c) = b =? ')

# 型キャスト
complex_a, complex_b = complex(str_a), complex(str_b) # 複素数型へ

# c := a + b * i
complex_c = complex_a + complex_b * 1j

# データとデータ型の確認
print('complex_c = ', complex_c, type(complex_c))

# cを2次元座標形式で一括入力
#https://stackoverflow.com/questions/17050222/input-a-list-of-2d-coordinates-in-python-from-user
import re # 正規表現

str_c = input('c = Re(c), Im(c) = ')
re_c, im_c = re.split(r'\W*\,\W*', str_c) # カンマと空白で分割
c = float(re_c) + float(im_c) * 1j # c := re_c + im_c * i
print('c = ', c, type(c))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
