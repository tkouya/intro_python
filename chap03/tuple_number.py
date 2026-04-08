# tuple_number.py: タプルを使って0から20まで表示する

# int_arrayタプルに0から20を入れる
int_array = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
int_array = (i for i in range(21))
print(int_array) # [, ]付きで出力

# int_arrayの中身をすべて表示
for num in int_array:
	print(num, end=' ')
print() # 最後に改行

# 逆順で表示→エラーになる
for num in reversed(int_array):
	print(num, end=' ')
print()
