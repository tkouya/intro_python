# variable.py: 変数とデータ型
a = 1               # 整数(integer)
b = True            # bool値（True か False)
c = -3.0            # 実数(float)
d = -2 + 5 * 1j     # 複素数(complex)
e = 'abcdefg'       # 文字列(ASCII文字)
f = '吾輩は猫である' # 文字列(UNICODE UTF-8)

print('a, type(a) = ', a, type(a))
print('b, type(b) = ', b, type(b))
print('c, type(c) = ', c, type(c))
print('d, type(d) = ', d, type(d))
print('e, type(e) = ', e, type(e))
print('f, type(e) = ', f, type(f))

print('a + b =', a + b)
print('a + b + c =', a + b + c)
print('a + b + c + d =', a + b + c + d)
#print('a + e =', a + e) # エラー
print('str(c) + e = ', str(c) + e)
print('e + f =', e + f)

a = 'ABCDE'
print('a, type(a) = ', a, type(a))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
