# output_complex.py: 複素数の書式付き出力
str_a = input('Re(c) = a =? ')
str_b = input('Im(c) = b =? ')

# 型キャスト
complex_a, complex_b = complex(str_a), complex(str_b) # 複素数型へ

# c := a + b * i
complex_c = complex_a + complex_b * 1j

# データとデータ型の確認
print('complex_c = ', complex_c)
print('complex_c = %g + %g * i' % (complex_c.real, complex_c.imag))
print('complex_c = {:g} + {:g} * i'.format(complex_c.real, complex_c.imag))
print(f'complex_c = {complex_c.real:g} + {complex_c.imag:g} * i')

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
