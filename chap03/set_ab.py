# set_ab.py: 集合演算
input_str = input('Input maxmum integer n =? ')
n = int(input_str)

# A = { n以下の4の倍数の集合 }
# B = { n以下の6の倍数の集合 }
A = set() # 空集合
B = set() # 空集合
for i in range(1, n + 1):
    if i % 4 == 0: A.add(i) # 要素iをAに追加
    if i % 6 == 0: B.add(i) # 要素iをBに追加

print('A = ', A)
print('B = ', B)

# ①和集合
print('A | B = ', A | B)
print('A.union(B) = ', A.union(B))

# ②積集合
print('A & B = ', A & B)
print('A.intersection(B) = ', A.intersection(B))

# ③和集合 - 積集合
print('A | B - A & B = ', (A | B) - (A & B))
print('(A.union(B)).difference(A.intersection(B)) = ', (A.union(B)).difference(A.intersection(B)))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# All rights reserved.
# -------------------------------------
