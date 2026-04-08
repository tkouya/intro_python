# graph/sin.py : Sineグラフの描画
from flask import Flask
from flask import render_template
from flask import request # methods as argument
from flask import redirect
from flask import Response
import numpy as np # NumPy
import matplotlib.pyplot as plt # グラフ描画ライブラリ

app = Flask(__name__)

# 固定ディレクトリ
PNG_DIR = 'static/'

# Cacheコントロール用
# https://stackoverflow.com/questions/45583828/python-flask-not-updating-images
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, public, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/draw', methods = ['GET', 'POST'])
def draw():
    x_min = request.form['x_min']
    x_max = request.form['x_max']
    div = int(request.form['div']) # 50
    graph_img_name = PNG_DIR + 'graph.png'

    # 計算とグラフ描画
    x_array = np.linspace(float(x_min), float(x_max), div)
    y_array = [np.sin(x) for x in x_array]
    fig, ax = plt.subplots()
    ax.plot(x_array, y_array)
    fig.savefig(graph_img_name)
    return render_template('index.html', x_min = x_min, x_max = x_max, img_name = graph_img_name, div = div)
