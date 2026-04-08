# input.py: フォーム入力の出力
from flask import Flask
from flask import render_template # 追加
from flask import request # 追加

app = Flask(__name__)

# トップへのアクセス
@app.route('/', methods=['GET', 'POST'])
def show_input():
    input = '入力なし'
    if request.method == 'POST':
        input = request.form['form_input']

    return render_template('index.html', mystr = input)
