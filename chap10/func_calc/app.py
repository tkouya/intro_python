# app.py : CSVファイルの描画
from flask import Flask
from flask import render_template
from flask import request # フォーム入力を受け取る
from numpy import * # NumPy関数を直接呼出し
import numexpr as ne # NumExpr: 式パーサ

app = Flask(__name__)

# 関数フォームを開く
@app.route('/')
def index():
    return render_template('index.html')

# 関数値の評価
@app.route('/calc', methods = ['POST']) # POSTでのみ受付
def calc():
    str_formula = request.form['input_formula']
    str_x = request.form['input_x']
    # 計算実行
    x = float(str_x) # xを数値に変換
    func_val = float(ne.evaluate(str_formula))
    # 計算結果を戻す
    return render_template('index.html', str_x = str_x, str_formula = str_formula, str_func_val=str(func_val))