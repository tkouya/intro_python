# object.py: 変数とオブジェクト

a = 2024 # (1)
print('aが参照しているオブジェクトのデータ型: ', type(a))
print('aが参照しているオブジェクトのID     : ', id(a))
b = a # (2)
print('bが参照しているオブジェクトのデータ型: ', type(b))
print('bが参照しているオブジェクトのID     : ', id(b))
print('a = ', a)
print('b = ', b)

a = 'This is a pen.' # (3)
print('aが参照しているオブジェクトのデータ型: ', type(a))
print('aが参照しているオブジェクトのID     : ', id(a))
print('bが参照しているオブジェクトのデータ型: ', type(b))
print('bが参照しているオブジェクトのID     : ', id(b))
print('a = ', a)
print('b = ', b)

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
