# read_write_file.py: テキストファイルを読み書きする

# ファイル名の指定
input_filename = 'student_grade_name.csv' # 読み込み用
output_filename = 'linenum_student_grade_name.txt' # 書き込み用

# ファイルを開く
with open(input_filename, 'r', encoding='utf-8') as f_in: # 読み込み用
    with open(output_filename, 'w', encoding='utf-8') as f_out: # 書き込み用
        # 1行ずつ読み込み
        num_line = 1
        while line := f_in.readline():
            # 標準出力
            print(f'{num_line:5d}:{line}', end=' ')
            # ファイル出力
            f_out.write(f'{num_line:5d}:{line}')
            num_line += 1

        # ファイルを閉じる
        f_out.close()
f_in.close()
