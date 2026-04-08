# while_ex.py: while文の例
# while文で0から20を正順と逆順に表示
min_num = 0
while min_num < 21:
	print(min_num, end=' ')
	min_num += 1
print()

# 逆順
max_num = 20
while max_num >= 0:
	print(max_num, end=' ')
	max_num -= 1
print()
