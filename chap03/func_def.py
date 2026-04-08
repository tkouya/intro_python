# func_def.py: 関数の定義

# f(x) = x^2 + 2x + 3
def func1(x): # xは引数
    return x ** 2 + 2 * x + 3 # 返り値

# f(x) = x^2 + 2*x + 3を表示
def func2(x):
    val = x**2 + 2 * x + 3
    print(f'func2({x:g}) = {val:g}')
    return # 返り値なし
