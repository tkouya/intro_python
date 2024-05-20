# print_number_for.py: forループを使って0から20まで表示する
for i in range(21):
	print(i, end=' ') # 改行の代わりにスペースを入れる
print() # 最後に改行

# int_arrayリストに0から20を入れる
int_array = [i for i in range(21)]
print(int_array) # [, ]付きで出力

# int_arrayの中身をすべて表示
for num in int_array:
	print(num, end=' ')
print() # 最後に改行

# 逆順で表示
for num in reversed(int_array):
	print(num, end=' ')
print()

# while文で逆順に表示
max_num = 20
while max_num >= 0:
	print(max_num, end=' ')
	max_num -= 1
print()
