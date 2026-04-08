# hellow.py: 最初のFlaskアプリ
from flask import Flask
from flask import render_template # 追加
from flask import request # 追加

app = Flask(__name__)

# トップへのアクセス
@app.route('/')
def hellow_world():
    #mojiretsu = 'ようこそ，Flaskの世界へ！'
    mojiretsu = '追手門学院大学へようこそ！'
    #print(mojiretsu) # ターミナルに出力
    #return mojiretsu # ブラウザに出力
    return render_template('index.html', mystr = mojiretsu)

