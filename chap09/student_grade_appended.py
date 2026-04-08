# student_grade.py: 生徒の成績統計計算
import numpy as np # NumPy
import pandas as pd # Pandas
import matplotlib.pyplot as plt # Matplotlib
#import japanize_matplotlib # Matplotlib日本語対応(old)
import matplotlib_fontja # Matplotlib日本語対応(New)

# Excelファイル名
filename = 'student_grade.xlsx'
# Excelシート名
sheetname = '学籍番号・氏名・タイトルなし'
# 教科名
subjects = ['国語', '英語', '数学', '理科', '社会']

# Excelファイル読み込み確認
try:
    pd.ExcelFile(filename)
except:
    print(filename, 'が開けませんでした。')

# Excelファイル読み込み時のみ動作
with pd.ExcelFile(filename) as xls:
    sheet = pd.read_excel(xls, sheetname)
    print(sheet)

    # 科目ごとの平均点，標準偏差，最高点，最低点
    for i in range(len(subjects)):
        print('{:s}の平均点，標準偏差，最高点，最低点: {:3.1f}, {:5.3g}, {:4d}, {:4d}'.format(
            subjects[i],
            np.average(sheet[subjects[i]]),
            np.std(sheet[subjects[i]]),
            np.amax(sheet[subjects[i]]),
            np.amin(sheet[subjects[i]])
        ))

    # 平均点のグラフ化
    x = subjects # ['国語', '英語', '数学', '理科', '社会']
    y = [np.average(sheet[x[i]]) for i in range(5)]
    fig, ax = plt.subplots()
    # 棒グラフ
    ax.set_title('科目別平均点')
    ax.set_ylabel('得点')
    ax.bar(x, y)
    # グラフ表示
    plt.show()

    # 生徒ごとの統計値
    student_name = input('生徒の氏名：')
    find_row = sheet.loc[sheet['氏名'] == student_name]

    # 生徒が見つかったときのみ動作
    if(find_row.empty == False):
        print(student_name, ' -> \n', find_row)
        #print(subjects[0], '::', find_row[subjects[0]].to_numpy()[0])
        #print(student_name, ' -> \n', find_row.to_numpy())
        #for i in range(len(subjects)):
        #    print(subjects[i], ' -> ', find_row[subjects[i]])

        #find_row_scores = find_row.loc[student_name, subjects[0]]
        find_row_scores = [find_row[subjects[i]].to_numpy()[0] for i in range(len(subjects))]
        print(find_row_scores)

        # 個人成績のグラフ化
        x = subjects # ['国語', '英語', '数学', '理科', '社会']
        y = find_row_scores # [find_row[x[i]] for i in range(5)]
        #print(y)
        fig, ax = plt.subplots()
        # 棒グラフ
        ax.set_title(student_name + 'の得点')
        ax.set_ylabel('得点')
        ax.bar(x, y)
        # グラフ表示
        plt.show()

        print(student_name, 'の平均点, 標準偏差，最高点，最低点: ',
            np.average(find_row_scores),
            np.std(find_row_scores),
            np.amax(find_row_scores),
            np.amin(find_row_scores)
        )

    else:
        print('名前: ', student_name, ' が見つかりません。')

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------

