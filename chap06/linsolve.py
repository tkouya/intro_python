# linsolve.py: 連立一次方程式を高速に解く
import numpy as np # NumPy
import scipy.linalg as sclinalg # Scipy.linalg
import time # time関数

# 乱数seedの指定
rng = np.random.default_rng(seed=20240521)

# 正方行列の次数
input_str = input('Input size of square matrix > ')
n = int(input_str)

# 乱数行列生成
mat_a = rng.random((n, n)) # n x n行列
print('||mat_a||_2 = ', np.linalg.norm(mat_a))
# 解を生成
true_x = rng.random((n, 1)) # n次元ベクトル
print('||x||_2 = ', np.linalg.norm(true_x))

# 定数ベクトルbを生成
b = mat_a @ true_x

# (1)逆行列を求めて連立一次方程式を解く
start_time = time.time()
inv_x = sclinalg.inv(mat_a) @ b
end_time_inv = time.time() - start_time
relerr_inv = np.linalg.norm(inv_x - true_x) / np.linalg.norm(true_x)

# (2) solve関数を用いて連立一次方程式を解く
start_time = time.time()
solve_x = sclinalg.solve(mat_a, b)
end_time_solve = time.time() - start_time
relerr_solve = np.linalg.norm(solve_x - true_x) / np.linalg.norm(true_x)

# ノルム相対誤差と計算時間の表示
print( '                           inv           solve')
print(f'Computational time (s): {end_time_inv:10.2g}, {end_time_solve:10.2g}')
print(f'Norm2 Relative error  : {relerr_inv:10.2e}, {relerr_solve:10.2e}')
