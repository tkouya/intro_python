# central_limit.py
import numpy as np # NumPy
import pandas as pd # Pandas
import matplotlib.pyplot as plt # Matplotlib
import japanize_matplotlib # Matplotlib日本語対応

# Excelファイル名
filename = 'central_limit.xlsx'
# Excelシート名
sheetname = '中心極限定理のグラフ化'

# Excelファイル読み込み確認
try:
    pd.ExcelFile(filename)
except:
    print(filename, 'が開けませんでした。')

# Excelファイル読み込み時のみ動作
with pd.ExcelFile(filename) as xls:
    sheet = pd.read_excel(xls, sheetname)

    # 母集団の統計値：キーボード入力
    str_mu = input('母集団の平均 = ? > ')
    str_sigma = input('母集団の標準偏差 = ? > ')
    mu = float(str_mu)
    sigma = float(str_sigma)

    # 「母集団の統計値」を作表する
    population = pd.Series({'平均': mu, '標準偏差': sigma, '分散': sigma**2})
    population.to_excel(filename, sheet_name=sheetname)

