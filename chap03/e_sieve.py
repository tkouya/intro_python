# e_sieve.py: エラトステネスの篩，素数を取り出し
input_str = input('Input integer =? ')
max_num = int(input_str)

# 素数を格納する
prime_number = [2] # 2以上を素数判定する

# メインループ
for i in range(3, max_num + 1):
    flag_prime = 0 # 0のままだと素数
    for pnum in prime_number:
        if i % pnum == 0:
            flag_prime = 1 # 素数でない
            break
    
    # 既存の素数にはないもの
    if flag_prime == 0:
        prime_number.append(i) # iを素数に追加

# 素数をリストアップ
print('Prime number (<', max_num, '):', prime_number)
