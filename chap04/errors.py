# errors.py: 誤差の計算
import numpy as np # NumPy

# 真値
x = np.sqrt(2.0)
print('True x = ', x)

# 近似値
approx_x = 1.4142
print('Approx x = ', approx_x)

# 誤差
Err = approx_x - x
print(f'E(Approx x) = {Err:10.2e}')

# 絶対誤差
aErr = np.abs(Err)
print(f'aE(Approx x) = {aErr:10.2e}')

# 相対誤差
rErr = aErr
if x != 0.0:
    rErr = aErr / np.abs(x)
print(f'rE(Approx x) = {rErr:10.2e}')

# 10進有効桁数
print(f'Sig. digits = {np.floor(-np.log10(rErr)):10.0g}')

