# quadratic_eq.py: 2次方程式を解く
#import math # sqrt関数
import mytool # quad_eq関数

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = float(a), float(b), float(c)
print(f'   {a:25.17g} * x^2')
print(f' + {b:25.17g} * x')
print(f' + {c:25.17g} = 0')

# ２次方程式を解く
mytool.quad_eq(a, b, c)
