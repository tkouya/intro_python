# e_sieve_func.py: エラトステネスの篩(関数呼び出し）
import mytool # prime_list関数定義

# メイン関数
input_str = input('Input integer =? ')
max_num = int(input_str)

# 素数リストを取得
prime_number = mytool.prime_list(max_num)

# 素数をリストアップ
print('Prime number (<=', max_num, '):', prime_number)
