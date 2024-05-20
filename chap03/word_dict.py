# word_dict.py: 辞書の例
mammal_dict = {'cat':'猫', 'dog':'犬', 'horse':'馬', 'cow':'牛', 'squerrel':'リス'}

# keyを使って値を取り出し
print('cat =>', mammal_dict['cat'])

# keyと値を同時に取り出し
for key, val in mammal_dict.items():
    print(key, '->', val)

