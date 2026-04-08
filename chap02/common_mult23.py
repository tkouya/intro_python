# common_mult23.py: 2と3の公倍数
a = int(input('a = ')) # 文字列入力→整数キャスト

if (a % 2 == 0) & (a % 3 == 0): # 2と3の公倍数
    print(a, ' is a common multiples of 2 and 3.')
elif a % 2 == 0: # 偶数
    print(a, ' is even.')
elif a % 3 == 0: # 3の倍数
    print(a, ' is a multiples of 3.')
else: # 上記以外
    print(a, ' is not even and a multiples of 3.')
