# power10.py: 10のべき乗判断
a = int(input('a = ')) # 文字列入力→整数キャスト

# 書き方1
if a == 1: # 1 = 10^0
    print('1 is a power of 10.')
elif a % 10 == 0: # 10のべき乗
    print(a, ' is a power of 10.')
else: 
    print(a, ' is not a power of 10.')
