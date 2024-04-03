# mytool.py: 独自定義の関数

# 第1章
# calc関数の定義
def calc(val1, val2):
    print('a = ', val1) # aの値を表示
    print('b = ', val2) # bの値を表示
    print('a + b, a - b, a * b, a / b = ', val1 + val2, val1 - val2, val1 * val2, val1 / val2)

# 第1章
# ret_calc関数の定義
def ret_calc(val1, val2):
    print('a = ', val1) # aの値を表示
    print('b = ', val2) # bの値を表示
    print('a + b, a - b, a * b, a / b = ', val1 + val2, val1 - val2, val1 * val2, val1 / val2)
    return val1 + val2, val1 - val2, val1 * val2, val1 / val2

# 第1章
# solve_1ji関数
# a * x + b = 0 -> x = -b / a
def solve_1ji(a, b):
    x = -b / a
    print('x = ', x)
    return x

# 第1章
# check_1ji関数
# a * x + b == 0 ?
def check_1ji(x, a, b):
    print('a * x + b = ', a * x + b)

# 第3章
# 素数リストを返す
def prime_list(maximum_num):
    # 素数を格納する
    in_prime_number = [2] # 2以上を素数判定する

    # メインループ
    for i in range(3, maximum_num + 1):
        flag_prime = 0 # 0のままだと素数
        for pnum in in_prime_number:
            if i % pnum == 0:
                flag_prime = 1 # 素数でない
                break
        
        # 既存の素数にはないもの
        if flag_prime == 0:
            in_prime_number.append(i) # iを素数に追加

    return in_prime_number

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
