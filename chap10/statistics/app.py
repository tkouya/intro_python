# flask\statistics\app.py : CSVファイルの描画
from flask import Flask
from flask import render_template
from flask import request # methods as argument
from flask import redirect
from flask import Response
import matplotlib # グラフ描画ライブラリ
matplotlib.use('Agg') # 再プロット時のエラー防止(GUI禁止)
import matplotlib.pyplot as plt # グラフ描画ライブラリ
import japanize_matplotlib # Matplotlib日本語対応
# pandas
import numpy as np # NumPy
import pandas as pd # Pandas

app = Flask(__name__)

# 固定ディレクトリ
PNG_DIR = 'static/'

# Cacheコントロール用
# https://stackoverflow.com/questions/45583828/python-flask-not-updating-images
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# 選択した生徒の成績
find_row_student = {}
find_row_scores = []

# Excelファイル名
filename = 'student_grade.xlsx'
# Excelシート名
sheetname = '学籍番号・氏名・タイトルなし'
# 教科名
subjects = ['国語', '英語', '数学', '理科', '社会']
# フィールド数(カラム数)
# 学籍番号，氏名，氏名読み仮名，教科名
max_num_column = 3 + len(subjects)
# 科目平均点グラフファイル名
subject_graph_name = 'subject_graph.png'
# 生徒別グラフファイル名
student_graph_name = 'student_graph.png'
# 選択した生徒の成績
#find_row_student = {}
# canvas_right, left_flag
canvas_right_flag = 0 # 存在なし
canvas_left_flag = 0 #

# 関数フォームを開く
@app.route('/')
@app.route('/index')
def index():
    # Excelファイル読み込み確認
    try:
        pd.ExcelFile(filename)
    except:
        print(filename, 'が開けませんでした。')

    # Excelファイル読み込み時のみ動作
    with pd.ExcelFile(filename) as xls:
        sheet = pd.read_excel(xls, sheetname)
        #print(sheet)

        # 科目ごとの平均点，標準偏差，最高点，最低点
        for i in range(len(subjects)):
            print('{:s}の平均点，標準偏差，最高点，最低点: {:3.1f}, {:5.3g}, {:4d}, {:4d}'.format(
                subjects[i],
                np.average(sheet[subjects[i]]),
                np.std(sheet[subjects[i]]),
                np.amax(sheet[subjects[i]]),
                np.amin(sheet[subjects[i]])
            ))

        # 平均点のグラフ化: subject_graph.png
        x = subjects # ['国語', '英語', '数学', '理科', '社会']
        y = [np.average(sheet[x[i]]) for i in range(5)]
        fig, ax = plt.subplots()
        # 棒グラフ
        ax.set_title('科目別平均点')
        ax.set_ylabel('得点')
        ax.bar(x, y)
        # グラフ表示
        #plt.show()
        # ファイルに書き出し
        plt.savefig(PNG_DIR + subject_graph_name)

        # 一行ごとに読み込み
        table = '<table>'
        print('sheet.shape: ', sheet.shape)
        for i in range(sheet.shape[0]):
            # table += '<tr><td>' + str(tuple(sheet.iloc[i, :])) + '</td></tr>'
            table += '<tr><td>'
            table += '<form action="/draw" method="POST">'
            table += '<input type="submit" value="グラフ描画">'
            table += str(tuple(sheet.iloc[i, :]))
            table += '<input type="hidden" name="student_id" value="' + sheet.iloc[i, 0] + '">'
            table += '</form>'
            table += '</td></tr>'
            print(tuple(sheet.iloc[i, :]))
 
        table += '</table>'

    return render_template('index.html', list = table)

# 関数グラフ描画
@app.route('/draw', methods = ['GET', 'POST'])
def draw():

    # 学生id取得
    student_id = request.form['student_id']

    # Excelファイル読み込み確認
    try:
        pd.ExcelFile(filename)
    except:
        print(filename, 'が開けませんでした。')

    # Excelファイル読み込み時のみ動作
    with pd.ExcelFile(filename) as xls:
        sheet = pd.read_excel(xls, sheetname)
        #print(sheet)

        # 科目ごとの平均点，標準偏差，最高点，最低点
        for i in range(len(subjects)):
            print('{:s}の平均点，標準偏差，最高点，最低点: {:3.1f}, {:5.3g}, {:4d}, {:4d}'.format(
                subjects[i],
                np.average(sheet[subjects[i]]),
                np.std(sheet[subjects[i]]),
                np.amax(sheet[subjects[i]]),
                np.amin(sheet[subjects[i]])
            ))

        # 平均点のグラフ化: subject_graph.png
        x = subjects # ['国語', '英語', '数学', '理科', '社会']
        y = [np.average(sheet[x[i]]) for i in range(5)]
        fig, ax = plt.subplots()
        # 棒グラフ
        ax.set_title('科目別平均点')
        ax.set_ylabel('得点')
        ax.bar(x, y)
        # グラフ表示
        #plt.show()
        # ファイルに書き出し
        plt.savefig(PNG_DIR + subject_graph_name)

        # 一行ごとに読み込み
        table = '<table>'
        print('sheet.shape: ', sheet.shape)
        for i in range(sheet.shape[0]):
            # table += '<tr><td>' + str(tuple(sheet.iloc[i, :])) + '</td></tr>'
            table += '<tr><td>'
            table += '<form action="/draw" method="POST">'
            table += '<input type="submit" value="グラフ描画">'
            table += str(tuple(sheet.iloc[i, :]))
            table += '<input type="hidden" name="student_id" value="' + sheet.iloc[i, 0] + '">'
            table += '</form>'
            table += '</td></tr>'
            print(tuple(sheet.iloc[i, :]))
            # 学生idの発見
            if sheet.iloc[i, 0] == student_id:
                find_row_student = sheet.iloc[i, 1]
                find_row_scores = [sheet.iloc[i, j] for j in range(3, 8)]
 
        table += '</table>'
        
        # 学生別グラフの描画
        #find_row_scores = []
        student_name = ''
        if len(find_row_student) > 0 :
            student_name = find_row_student
            #find_row_scores = [find_row_student[subjects[i]] for i in range(len(subjects))]
            print('find_row_scores = ', find_row_scores)
        
        # 個人成績のグラフ化
        x = subjects # ['国語', '英語', '数学', '理科', '社会']
        y = find_row_scores # [find_row[x[i]] for i in range(5)]
        #print(y)
        fig_right, ax = plt.subplots()
        # 棒グラフ
        ax.set_title(student_name + 'の得点')
        ax.set_ylabel('得点')
        if len(student_name) > 0:
            ax.bar(x, y)
        # グラフ表示
        #plt.show()
        plt.savefig(PNG_DIR + student_graph_name)

    print('graph1, graph2 = ', student_graph_name, subject_graph_name)
    return render_template('index.html', list = table, graph1 = PNG_DIR + student_graph_name, graph1_comment = '学生データ', graph2 = PNG_DIR + subject_graph_name, graph2_comment = '教科別')
