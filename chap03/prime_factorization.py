# prime_factorization.py: 素因数分解
import mytool

# メイン関数
input_str = input('Input integer =? ')
int_num = int(input_str)

# 素数リストを取得
prime_number = mytool.prime_list(int_num)

# 素数をリストアップ
print('Prime number (<', int_num, '):', prime_number)

# 素因数リスト
factlist = []
new_int_num = int_num
for prime in prime_number:
    while (new_int_num % prime == 0) & (new_int_num >= 2):
        factlist.append(prime)
        new_int_num /= prime

# 検算と素因数分解
print('Original integer      = ', int_num)
print('Product of prime list = ', mytool.product_list(factlist), ' = ', factlist)

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
