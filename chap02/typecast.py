# typecast.py: 型キャスト例
str_a = input('a =? ')
str_b = input('b =? ')

# 型キャスト
int_a, int_b = int(str_a), int(str_b) # 整数型へ
float_a, float_b = float(str_a), float(str_b) # 実数型へ
complex_a, complex_b = complex(str_a), complex(str_b) # 複素数型へ

# データとデータ型の確認
print('int_a, type(int_a) = ', int_a, type(int_a))
print('float_a, type(float_a) = ', float_a, type(float_a))
print('complex_a, type(fcomplex_a) = ', complex_a, type(complex_a))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
