# prime_factorization_gmpy2.py: 素因数分解をGMPで行う
import gmpy2 # 高速多倍長精度パッケージ with GMP, MPFR and MPC
import time # 時間計測

# ---
# main
# ---
input_str = input('Input integer > ')
max_num = int(input_str)

# 時間計測開始
start_time = time.time()

# 素数のリスト表示
plist = [gmpy2.mpz(2)]
while max_num > plist[-1]: # 最大の素数との比較
    plist.append(gmpy2.next_prime(plist[-1]))

#print('Prime number = ', plist)

# 素因数のリスト
factlist = [] # 空にしておく

# 因数のチェック
n = gmpy2.mpz(max_num) # mpz型に変換
for pnum in plist:
    while gmpy2.is_divisible(n, pnum): # 割り切れるか？
        factlist.append(pnum)
        n = gmpy2.divexact(n, pnum) # n /= pnum

# 素因数リスト
print(f'{max_num:d} = ')
print(factlist)

# 検算
prod = 1
for fact in factlist:
    prod *= fact

print('original = ', max_num)
print('factlist = ', prod)

# 時間計測終了
total_time = time.time() - start_time

print(f'total_time(s): {total_time:g}')
