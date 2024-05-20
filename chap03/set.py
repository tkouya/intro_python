# set.py: 集合の使い方
input_str = input('Input maxmum integer n =? ')
n = int(input_str)

# A = { n以下の偶数の集合 }
# B = { n以下の3の倍数の集合 }
A = set() # 空集合
B = set() # 空集合
for i in range(1, n + 1):
    if i % 2 == 0: A.add(i) # 要素iをAに追加
    if i % 3 == 0: B.add(i) # 要素iをBに追加

print('A = ', A)
print('B = ', B)

# 和集合
print('A | B = ', A | B)
print('A.union(B) = ', A.union(B))

# 積集合
print('A & B = ', A & B)
print('A intersection B = ', A.intersection(B))

# 差集合
print('A - B = ', A - B)
print('A.differernce(B) = ', A.difference(B))

# 要素の削除
print('A.discard(2) = ', A.discard(2))
print('A.remove(2)  = ', A.remove(2)) # エラーになる

# 対象差集合
print('A ^ B = ', A ^ B)
print('A.symmetric_difference(B) = ', A.symmetric_difference(B))
print('(A - (A & B)) | (B - (A & B)) = ', (A - (A & B)) | (B - (A & B)))

