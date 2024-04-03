# simple_calc2.py: 加減乗除結果を表示(関数化)

# calc関数の定義
def calc(val1, val2):
    print('a = ', val1) # aの値を表示
    print('b = ', val2) # bの値を表示
    print('a + b, a - b, a * b, a / b = ', val1 + val2, val1 - val2, val1 * val2, val1 / val2)

# メイン関数部分
calc(10, 3) # a = 10, b = 3
calc(3, 4)  # a = 3, b = 4

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
