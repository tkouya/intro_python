# central_limit.py
import numpy as np # NumPy
import pandas as pd # Pandas
import scipy.stats as scstats # SciPy.stats
import matplotlib.pyplot as plt # Matplotlib
import japanize_matplotlib # Matplotlib日本語対応

# Excelファイル名
filename = 'central_limit.xlsx'
# Excelシート名
sheetname = '中心極限定理のグラフ化'

# 母集団の統計値：キーボード入力
str_mu = input('母集団の平均 = ? > ')
str_sigma = input('母集団の標準偏差 = ? > ')
mu = float(str_mu)
sigma = float(str_sigma)

# 「母集団の統計値」を作表する
population = pd.Series({'平均': mu, '標準偏差': sigma, '分散': sigma**2})

# 「標本の統計値」を作表する
str_x_bar = input('標本平均 = ? > ')
x_bar = float(str_x_bar)

# 標本数 : 2^1, ..., 2^10
num_sample = 10
num_samples = [2**i for i in range(1, num_sample+1)]

# normインスタンス
norm_dists = [
    scstats.norm(loc=mu, scale=sigma/np.sqrt(num_samples[i])).sf(x_bar)
    for i in range(num_sample)
]

# 標本の統計値テーブルを作る
sample = pd.DataFrame(data = {
        '標本数': num_samples,
        '標本平均': [x_bar for i in range(num_sample)],
        '標本平均以上になる確率': norm_dists
    }
)

# Excelファイル書き出し
with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    # 表の書き出し
    sample.to_excel(writer, sheet_name=sheetname, startrow=6, header=True)
    population.to_excel(writer, sheet_name=sheetname, startrow=1, index=False)
    # 表タイトルの書き出し
    worksheet = writer.sheets[sheetname]
    #worksheet.cell(row=1, column=1).value = '母集団の統計値'
    #worksheet.cell(row=6, column=1).value = '標本の統計値'
    #writer.save() # 書き出し
