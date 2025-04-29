# print_number_loop.py: ループを使って0から20まで表示する
for i in range(21):
	print(i, end=' ') # 改行の代わりにスペースを入れる
print() # 最後に改行

# while文で0から20まで表示
max_num = 0
while max_num <= 20:
	print(max_num, end=' ')
	max_num += 1 # max_numを１ずつ増やす
print() # 最後に改行

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------

