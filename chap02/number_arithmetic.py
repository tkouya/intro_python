# number_arithmetic.py: 整数，実数，複素数の四則演算
int_a, int_b = 1, 2
float_a, float_b = 1.0, 2.0
complex_a, complex_b = 1.0 + 0 * 1j, complex(2.0, 0.0) # 3.0 + 4.0 * 1j, complex(-2, -5)

print('int_a, int_b =         ', int_a, int_b)
print('float_a, float_b =     ', float_a, float_b)
print('complex_a, complex_b = ', complex_a, complex_b)

# 同じデータ型どうしの四則演算
print('a + b = ', int_a + int_b, float_a + float_b, complex_a + complex_b)
print('a - b = ', int_a - int_b, float_a - float_b, complex_a - complex_b)
print('a * b = ', int_a * int_b, float_a * float_b, complex_a * complex_b)
print('a / b = ', int_a / int_b, float_a / float_b, complex_a / complex_b)

# データ型混合四則演算
print('a + b = ', int_a + float_b, float_a + complex_b, complex_a + int_b)
print('a - b = ', int_a - float_b, float_a - complex_b, complex_a - int_b)
print('a * b = ', int_a * float_b, float_a * complex_b, complex_a * int_b)
print('a / b = ', int_a / float_b, float_a / complex_b, complex_a / int_b)
