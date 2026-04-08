# func_main.py: 関数モジュールの呼び出し
import func_def # (1) 別名なし
import func_def as f # (2) fという別名を付ける
from func_def import func1, func2 # (3) 同一名前空間

# メイン関数

# (1) 別名なし
print('func_def.func1(3) = ', func_def.func1(3))
func_def.func2(3)

# (2) 別名あり
print('f.func1(3) = ', f.func1(3))
f.func2(3)

# (3) 同一名前空間
print('func1(3) = ', func1(3))
func2(3)
