# mult3.py: 偶奇判断
a = int(input('a = ')) # 文字列入力→整数キャスト

# 書き方1
if a % 2 == 0: # 偶数
    print(a, ' is even.')
else: # 奇数
    print(a, ' is odd.')

# 書き方2
if a % 2 != 0: # 奇数
    print(a, ' is odd.')
else: # 偶数
    print(a, ' is even.')
