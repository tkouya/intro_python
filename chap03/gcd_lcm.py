# gcd_lcm.py: 最大公約数と最小公倍数
import mytool # prime_fact関数追加

m = input('m =? ')
n = input('n =? ')
m, n = int(m), int(n)

# 素因数分解リスト表示
factlist_m = mytool.prime_fact(m)
factlist_n = mytool.prime_fact(n)
print('factlist_m = ', factlist_m)
print('factlist_n = ', factlist_n)

gcdlist = []

# 最大公約数
start_j = 0
for i in range(len(factlist_m)):
    print('start_j = ', start_j)
    for j in range(start_j, len(factlist_n)):
        if factlist_m[i] == factlist_n[j]:
            gcdlist.append(factlist_m[i])
            start_j = j + 1 # 見つかったら削る
            print('i, j = ', i , ', ', j)
            break

# gcdlist確認
print('gcdlist = ', gcdlist)

# 最小公倍数
# factlist_mとfactlist_nから
# gcdlistを削った残りを取り出す
for pnum in gcdlist:
    for i in range(len(factlist_m)):
        if factlist_m[i] == pnum:
            factlist_m.pop(i) # i番目を削除
            break

    for i in range(len(factlist_n)):
        if factlist_n[i] == pnum:
            factlist_n.pop(i) # i番目を削除
            break

# lcmlist = gcdlist + factlist_m + factlist_n
lcmlist = gcdlist + factlist_m + factlist_n
print('lcmlist = ', lcmlist)

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
