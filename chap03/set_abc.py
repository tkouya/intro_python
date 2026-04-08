# set_abc.py: 集合演算
input_str = input('Input maxmum integer n =? ')
n = int(input_str)

# A = { n以下の5の倍数の集合 }
# B = { n以下の6の倍数の集合 }
# C = { n以下の7の倍数の集合 }
A = set() # 空集合
B = set() # 空集合
C = set() # 空集合
for i in range(1, n + 1):
    if i % 5 == 0: A.add(i) # 要素iをAに追加
    if i % 6 == 0: B.add(i) # 要素iをBに追加
    if i % 7 == 0: C.add(i) # 要素iをCに追加

print('A = ', A)
print('B = ', B)
print('C = ', C)

# ①和集合
print('A | B | C = ', A | B | C)
print('A.union(B).union(C) = ', A.union(B).union(C))

# ②積集合
print('A & B & C = ', A & B & C)
print('A.intersection(B) = ', A.intersection(B).intersection(C))

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
