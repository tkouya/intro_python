# example_myaddress.py: アドレス帳使用例
from address_class import MyAddress # MyAddressクラス定義

# メイン関数

# aiとotaはMyAddressインスタンス
ai = MyAddress(1, '安威太郎', 'あいたろう', '茨木市西安威２丁目')
ota = MyAddress(2, '太田次郎', 'おおたじろう', '茨木市太田東芝町１－１')

# 住所録表示
ai.print_all()
ota.print_all()

# 文字列化
print(str(ai))
print(ota)
