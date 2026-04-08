# mytool.py: 2次方程式を解く
import math # sqrt関数

# 2次方程式 ax^2 + bx + c = 0 を解く
def quad_eq(a, b, c):
    # 判別式の計算
    d = b**2 - 4 * a * c

    if d >= 0:
        print('Real solutions: \n')
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'x1 = {x1:25.17e}')
        print(f'x2 = {x2:25.17e}')
    else:
        print('complex solutions: \n')
