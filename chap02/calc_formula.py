# calc_formula.py: 数式に基づく計算
import math
import cmath

# exp((-4/3)^3) = e^{(-4/3)^3}
print('exp((-4/3)^3) = ', math.exp((-4/3)**3))

# sqrt(-5)
print('sqrt(-5) = ', cmath.sqrt(-5 + 0 * 1j))

# exp(log(-10))
print('exp(log(-10)) = ', cmath.exp(cmath.log(-10 + 0 * 1j)))

# i^i
print('i^i = ', (0 + 1j) ** (0 + 1j))

# -------------------------------------
# Copyright (c) 2024 Tomonori Kouya
# https://github.com/tkouya/intro_python
# -------------------------------------
